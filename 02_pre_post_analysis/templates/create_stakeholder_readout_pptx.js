const pptxgen = require('pptxgenjs');

const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = 'Analytics Standard Framework';
pptx.subject = 'Pre/Post stakeholder readout template';
pptx.title = 'Pre/Post Impact Analysis Stakeholder Readout Template';
pptx.company = 'Portfolio / Training Template';
pptx.lang = 'en-US';
pptx.theme = {
  headFontFace: 'Aptos Display',
  bodyFontFace: 'Aptos',
  lang: 'en-US'
};
pptx.defineLayout({ name: 'CUSTOM_WIDE', width: 13.333, height: 7.5 });
pptx.layout = 'CUSTOM_WIDE';
pptx.margin = 0;
pptx.slideWidth = 13.333;
pptx.slideHeight = 7.5;
pptx.subject = 'Reusable Pre/Post Analysis deck template';

const C = {
  navy: '122337',
  blue: '2865A8',
  teal: '16968E',
  gold: 'F3AD3F',
  gray: '5F6973',
  light: 'F5F7FA',
  white: 'FFFFFF',
  green: '33915B',
  border: 'D6DDE6'
};

function title(slide, title, subtitle) {
  slide.addText(title, { x: 0.65, y: 0.35, w: 12, h: 0.5, fontFace: 'Aptos Display', fontSize: 28, bold: true, color: C.navy, margin: 0 });
  if (subtitle) slide.addText(subtitle, { x: 0.68, y: 0.88, w: 11.8, h: 0.35, fontSize: 12, color: C.gray, margin: 0 });
}

function footer(slide, n) {
  slide.addShape(pptx.ShapeType.rect, { x: 0, y: 7.18, w: 13.333, h: 0.04, fill: { color: C.blue }, line: { color: C.blue } });
  slide.addText('Pre/Post Analysis Standard Framework | Stakeholder Readout Template', { x: 0.65, y: 7.22, w: 9, h: 0.22, fontSize: 8, color: C.gray, margin: 0 });
  slide.addText(String(n), { x: 12.3, y: 7.22, w: 0.45, h: 0.22, fontSize: 8, color: C.gray, align: 'right', margin: 0 });
}

function callout(slide, x, y, w, label, value, color = C.blue) {
  slide.addShape(pptx.ShapeType.roundRect, { x, y, w, h: 1.05, rectRadius: 0.08, fill: { color: C.light }, line: { color: C.border } });
  slide.addText(label.toUpperCase(), { x: x + 0.16, y: y + 0.13, w: w - 0.32, h: 0.25, fontSize: 8, bold: true, color: C.gray, margin: 0 });
  slide.addText(value, { x: x + 0.16, y: y + 0.42, w: w - 0.32, h: 0.4, fontSize: 18, bold: true, color, margin: 0 });
}

function bullets(slide, items, x, y, w, h, size = 15) {
  slide.addText(items.map(t => ({ text: t, options: { bullet: { type: 'ul' } } })), { x, y, w, h, fontSize: size, color: C.navy, breakLine: true, fit: 'shrink', valign: 'top' });
}

function table(slide, rows, x, y, w, h, colW) {
  slide.addTable(rows, { x, y, w, h, colW, border: { color: C.border, pt: 0.6 }, fontFace: 'Aptos', fontSize: 9, color: C.navy, valign: 'mid' });
}

function addStandardSlides() {
  let s = pptx.addSlide();
  s.background = { color: C.navy };
  s.addText('Pre/Post Impact Analysis', { x: 0.8, y: 1.25, w: 8.2, h: 0.9, fontSize: 44, bold: true, color: C.white, margin: 0 });
  s.addText('Stakeholder readout template for interventions without randomized Control groups', { x: 0.83, y: 2.45, w: 8.6, h: 0.7, fontSize: 18, color: 'DCE6F0', margin: 0 });
  callout(s, 0.82, 4.7, 2.5, 'Business question', '[insert]', C.gold);
  callout(s, 3.55, 4.7, 2.5, 'Launch date', '[insert]', C.gold);
  callout(s, 6.28, 4.7, 2.5, 'Recommendation', '[insert]', C.gold);
  footer(s, 1);

  s = pptx.addSlide(); title(s, 'Executive Summary', 'Lead with the decision, then support it with evidence.');
  callout(s, .75, 1.35, 2.4, 'Observed KPI Change', '+X.X pp', C.teal);
  callout(s, 3.38, 1.35, 2.4, 'Adjusted Evidence', 'Moderate', C.blue);
  callout(s, 6.01, 1.35, 2.4, 'Guardrails', 'Stable', C.green);
  callout(s, 8.64, 1.35, 2.4, 'Decision', 'Continue', C.gold);
  bullets(s, ['After launch, [primary KPI] changed from [Pre] to [Post] ([absolute lift] pp).', 'After accounting for trend, ramp, seasonality, campaign timing, and traffic mix, the evidence suggests [causal confidence].', 'Guardrails show [no material deterioration / specific concern].', 'Recommendation: [continue / monitor / iterate / validate further / rollback].'], .85, 3.05, 11.6, 2.7, 16);
  footer(s, 2);

  s = pptx.addSlide(); title(s, 'Business Question & Analysis Design', 'Explain what changed and why there is no randomized Control group.');
  bullets(s, ['Business question: Did [intervention] improve [primary KPI] without harming guardrails?', 'Intervention launch: [date].', 'Rollout design: 100% of eligible population; no randomized Control group.', 'Pre period: [date range]. Post period: [date range].', 'Causal risk: baseline trend, seasonality, traffic mix, ramp, and concurrent events.'], .8, 1.35, 5.8, 4.7, 15);
  footer(s, 3);

  s = pptx.addSlide(); title(s, 'Measurement Framework', 'Define success and risk before interpreting results.');
  table(s, [
    [{ text: 'KPI Type', options: { fill: { color: C.navy }, color: C.white, bold: true } }, { text: 'Metric', options: { fill: { color: C.navy }, color: C.white, bold: true } }, { text: 'Direction', options: { fill: { color: C.navy }, color: C.white, bold: true } }, { text: 'Why it matters', options: { fill: { color: C.navy }, color: C.white, bold: true } }],
    ['Primary', '[Verification completion rate]', 'Higher', 'Direct success measure'],
    ['Secondary', '[Verification time]', 'Lower', 'Customer/operational friction'],
    ['Secondary', '[Manual review rate]', 'Lower', 'Expected mechanism of automation'],
    ['Guardrail', '[Payment decline rate]', 'Stable', 'Payment quality / approval risk'],
    ['Guardrail', '[Fraud-confirmed rate]', 'Stable/lower', 'Risk control']
  ], .75, 1.35, 11.8, 3.4, [2, 3.2, 1.5, 5.1]);
  footer(s, 4);

  s = pptx.addSlide(); title(s, 'Data Quality & Analytical Population', 'Establish trust before showing results.');
  table(s, [
    [{ text: 'Check', options: { fill: { color: C.navy }, color: C.white, bold: true } }, { text: 'Status', options: { fill: { color: C.navy }, color: C.white, bold: true } }, { text: 'Decision relevance', options: { fill: { color: C.navy }, color: C.white, bold: true } }],
    ['Duplicate IDs', 'Corrected', 'Avoid double-counting transactions'],
    ['Missing critical fields', 'Reviewed', 'Identify bias risk'],
    ['Intervention flags', 'Re-derived', 'Use transaction date as source of truth'],
    ['Duration anomalies', 'Excluded for duration metrics', 'Avoid distorted averages'],
    ['Final population', '[N rows]', 'Basis for all results']
  ], .75, 1.35, 11.8, 3.5, [3, 2.2, 6.6]);
  footer(s, 5);

  ['Simple Pre/Post Results', 'Trend, Ramp, and Concurrent Events', 'Confounders & Traffic-Mix Shift', 'Interrupted Time Series Evidence', 'Guardrails & Trade-Offs', 'Business Impact', 'Recommendation & Next Steps'].forEach((name, i) => {
    s = pptx.addSlide(); title(s, name, 'Replace placeholder content with analysis outputs and decision-ready interpretation.');
    callout(s, .8, 1.35, 3, 'Key message', '[insert]', i % 2 ? C.blue : C.teal);
    bullets(s, ['What changed?', 'How credible is the evidence?', 'What alternative explanations were evaluated?', 'What should stakeholders do next?'], .9, 3.0, 11.2, 2.8, 18);
    footer(s, 6 + i);
  });
}

addStandardSlides();
pptx.writeFile({ fileName: 'pre_post_stakeholder_readout_template.pptx' });
