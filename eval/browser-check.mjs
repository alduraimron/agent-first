// Run inside approved OMP JavaScript eval after opening an owned native Tern tab.
// Inspect the native open result in a separate call before confirming its backend.
export async function checkTaskUi({tab, backend, url, output, write, print}) {
  const result = {status: 'FAIL', url, requestedBackend: 'tern', actualBackend: backend, checks: [],
    backendEvidence: 'Caller inspected the preceding native browser.open result before this check',
    manualAccessibility: {status: 'NOT-RUN', reason: 'No screen reader or full accessibility audit executed'}};
  if (!tab) throw new Error('An already opened owned tab is required');
  const check = (name, passed, evidence) => {
    result.checks.push({name, status: passed ? 'PASS' : 'FAIL', evidence});
    if (!passed) throw new Error(name);
  };
  try {
    if (backend !== 'tern') {
      result.status = 'NOT-RUN';
      throw new Error('Actual native backend was not confirmed as Tern');
    }
    result.initialObservation = await tab.observe();
    const semantics = await tab.evaluate(() => {
      const input = document.querySelector('input');
      return {form: Boolean(input?.form), label: Array.from(input?.labels || []).map(x => x.textContent.trim()).join(' '),
        liveRegions: document.querySelectorAll('[aria-live], [role="status"], [role="alert"]').length};
    });
    check('visible-associated-label-and-form', semantics.form && semantics.label.length > 0, semantics);
    await tab.focus('input');
    await tab.press('Enter', {selector: 'input'});
    const invalid = await tab.evaluate(() => {
      const input = document.querySelector('input');
      const ids = [input.getAttribute('aria-describedby'), input.getAttribute('aria-errormessage')].filter(Boolean).join(' ').split(/\s+/);
      const associated = ids.map(id => document.getElementById(id)).filter(node => node && !node.hidden
        && getComputedStyle(node).display !== 'none').map(node => node.textContent.trim()).join(' ');
      return {message: (input.validationMessage || associated).trim(),
        invalid: input.getAttribute('aria-invalid') === 'true' || !input.validity.valid,
        inputFocused: document.activeElement === input};
    });
    check('empty-keyboard-submit-gives-feedback', invalid.invalid && invalid.message.length > 0 && invalid.inputFocused, invalid);
    const text = '<img src=x onerror="document.body.dataset.exploited=1"> ' + Date.now();
    await tab.fill('input', text);
    await tab.press('Enter', {selector: 'input'});
    await tab.waitForText(text, {timeout: 10000});
    const submitted = await tab.evaluate(async () => {
      const input = document.querySelector('input');
      return {rows: await fetch('/api/tasks').then(r => r.json()),
        inputFocused: document.activeElement === input, inputValue: input.value,
        injectedImages: document.querySelectorAll('li img').length,
        exploited: document.body.dataset.exploited || null,
        liveText: Array.from(document.querySelectorAll('[aria-live], [role="status"], [role="alert"]')).map(x => x.textContent.trim()).join(' ')};
    });
    check('keyboard-submission-persists-through-real-api', submitted.rows.some(row => row.text === text), submitted.rows);
    check('markup-is-rendered-as-text', submitted.injectedImages === 0 && submitted.exploited === null,
      {injectedImages: submitted.injectedImages, exploited: submitted.exploited});
    check('success-focus-and-live-feedback', submitted.inputFocused && submitted.inputValue === '' && submitted.liveText.length > 0,
      {inputFocused: submitted.inputFocused, inputValue: submitted.inputValue, liveText: submitted.liveText});
    await tab.press('Tab');
    const submitReachable = await tab.evaluate(() => {
      const input = document.querySelector('input');
      return document.activeElement === input.form.querySelector('button[type="submit"], button:not([type]), input[type="submit"]');
    });
    await tab.press('Shift+Tab');
    const inputReachable = await tab.evaluate(() => document.activeElement === document.querySelector('input'));
    check('keyboard-tab-order', submitReachable && inputReachable, {submitReachable, inputReachable});
    await tab.reload();
    await tab.waitForText(text, {timeout: 10000});
    check('reload-recovers-server-state', (await tab.text()).includes(text), await tab.observe());
    const errors = await tab.errors();
    check('no-page-errors', errors.entries.length === 0, errors);
    result.viewport = await tab.evaluate(() => ({width: innerWidth, height: innerHeight, dpr: devicePixelRatio,
      scrollWidth: document.documentElement.scrollWidth}));
    const screenshot = await tab.screenshot({fullPage: true});
    result.screenshot = typeof screenshot === 'string' ? screenshot : screenshot?.path || 'See native screenshot output';
    if (print) print(screenshot);
    result.status = 'PASS';
  } catch (error) {
    result.error = String(error);
  } finally {
    if (tab) {
      try { await tab.close(); result.ownedTabClosed = true; }
      catch (error) { result.ownedTabClosed = false; result.status = 'FAIL'; result.cleanupError = String(error); }
    }
    await write(output, JSON.stringify(result, null, 2) + '\n');
  }
  return result;
}
