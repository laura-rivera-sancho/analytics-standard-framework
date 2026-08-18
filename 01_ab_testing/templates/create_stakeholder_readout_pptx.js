const pptxgen = require('pptxgenjs');

const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = 'Laura Rivera Sancho';
pptx.company = 'Analytics Standard Framework';
pptx.subject = 'Reusable stakeholder readout template for A/B testing results';
pptx.theme = { headFontFace: 'Aptos Display', bodyFontFace: 'Aptos', lang: 'en-US' };

const C = {
  navy: '17324D', ink: '1E293B', gray: '64748B', line: 'CBD5E1',
  blue: '2F6FED', teal: '0F9B8E', green: '1C7C54', amber: 'D97706', white: 'FFFFFF'
};

function text(slide, value, x, y, w, h, options = {}) {
  slide.addText(value, {
    x, y, w, h,
    fontFace: options.face || 'Aptos',
    fontSize: options.size || 11,
    color: options.color || C.ink,
    bold: options.bold || false,
    italic: options.italic || false,
    align: options.align || 'left',
    valign: 'top',
    margin: 0,
    fit: 'shrink'
  });
}

function header(slide, section, title, page) {
  text(slide, section, 0.55, 0.28, 1.8, 0.25, { size: 8, bold: true, color: C.blue });
  text(slide, title, 0.55, 0.55, 8.8, 0.44, { size: 22, bold: true, color: C.navy, face: 'Aptos Display' });
  text(slide, 'A/B Testing Stakeholder Readout Template', 9.4, 0.34, 3.2, 0.25, { size: 8, color: C.gray, align: 'right' });
  slide.addShape(pptx.ShapeType.line, { x: 0.55, y: 1.05, w: 12.25, h: 0, line: { color: C.line, width: 0.75 } });
  text(slide, String(page).padStart(2, '0'), 12.35, 7.08, 0.45, 0.2, { size: 8, color: C.gray, align: 'right' });
}

function box(slide, value, x, y, w, h, color = C.line) {
  slide.addShape(pptx.ShapeType.roundRect, {
    x, y, w, h, rectRadius: 0.06,
    fill: { color: 'FFFFFF', transparency: 100 },
    line: { color, width: 1, dash: 'dash' }
  });
  text(slide, value, x + 0.12, y + 0.12, w - 0.24, Math.min(0.55, h - 0.12), { size: 9, color: C.gray, italic: true });
}

function label(slide, value, x, y, w = 3) {
  text(slide, value, x, y, w, 0.2, { size: 10, bold: true, color: C.blue });
}

function check(slide, value, x, y, w) {
  text(slide, '✓', x, y, 0.18, 0.25, { size: 11, bold: true, color: C.green });
  text(slide, value, x + 0.25, y, w, 0.25, { size: 10.5 });
}

function miniRows(slide, headers, rows, x, y, w, rowH) {
  const colW = w / headers.length;
  headers.forEach((h, i) => text(slide, h, x + i * colW, y, colW - 0.08, 0.22, { size: 8.5, bold: true, color: C.gray }));
  slide.addShape(pptx.ShapeType.line, { x, y: y + 0.3, w, h: 0, line: { color: C.line, width: 0.75 } });
  rows.forEach((row, r) => row.forEach((cell, i) => text(slide, cell, x + i * colW, y + 0.42 + r * rowH, colW - 0.08, rowH - 0.03, { size: 8.8 })));
}

function addSlide(title, section, page, build) {
  const slide = pptx.addSlide();
  header(slide, section, title, page);
  build(slide);
  return slide;
}

// 1. Cover
let slide = pptx.addSlide();
slide.addShape(pptx.ShapeType.rect, { x: 0, y: 0, w: 4.15, h: 7.5, fill: { color: C.navy }, line: { color: C.navy } });
slide.addShape(pptx.ShapeType.rect, { x: 4.15, y: 0, w: 0.12, h: 7.5, fill: { color: C.blue }, line: { color: C.blue } });
text(slide, 'A/B TESTING', 0.58, 0.75, 2.4, 0.3, { size: 11, bold: true, color: 'A8C7FA' });
text(slide, 'Stakeholder\nReadout Template', 0.58, 1.25, 3.0, 1.7, { size: 30, bold: true, color: C.white, face: 'Aptos Display' });
text(slide, 'Standard template for communicating controlled-experiment results with business impact and recommendations.', 0.6, 3.45, 2.85, 0.85, { size: 12, color: 'DCE8F6' });
text(slide, 'Analytics Standard Framework', 0.6, 6.65, 2.8, 0.25, { size: 9, color: 'DCE8F6' });
text(slide, 'How to use this deck', 4.9, 0.85, 4.4, 0.38, { size: 20, bold: true, color: C.navy, face: 'Aptos Display' });
text(slide, 'Replace placeholders with experiment-specific evidence. Keep the story decision-focused: what happened, does it matter, and what should we do?', 4.9, 1.35, 6.6, 0.8, { size: 12 });
label(slide, 'Recommended storyline', 4.9, 2.4);
['Business question', 'Experiment design', 'Experiment health', 'Primary result', 'Guardrails and segments', 'Business impact', 'Recommendation and next steps'].forEach((item, i) => check(slide, item, 5.0, 2.8 + i * 0.43, 4.2));
box(slide, 'Add logo or client / product name here', 9.65, 5.8, 2.6, 0.7);
text(slide, '01', 12.35, 7.08, 0.45, 0.2, { size: 8, color: C.gray, align: 'right' });

// 2. Executive Summary
addSlide('Executive Summary', '01 / DECISION FIRST', 2, s => {
  text(s, 'Use this slide to answer the main stakeholder question before presenting methodology.', 0.65, 1.28, 6.4, 0.35, { size: 11, color: C.gray });
  box(s, 'Recommendation headline: Roll out / Iterate / Retest / Stop', 0.65, 1.85, 6.0, 0.75, C.blue);
  label(s, 'Result snapshot', 0.65, 3.0);
  miniRows(s, ['Metric', 'Control', 'Treatment', 'Lift', 'Evidence'], [['Primary KPI', '[x%]', '[y%]', '[+z pp]', '[CI / p]'], ['Guardrails', '[status]', '[status]', '[change]', '[interpretation]']], 0.65, 3.35, 6.0, 0.45);
  label(s, 'Executive message', 7.3, 1.28);
  text(s, 'The Treatment [increased/decreased] [primary KPI] by [X percentage points] versus Control. The effect was [statistically significant / not significant] and [met / did not meet] the predefined business threshold. Guardrails showed [no material deterioration / specific risk].', 7.3, 1.65, 4.95, 2.35, { size: 15, color: C.navy });
  box(s, 'Decision / impact callout', 7.3, 4.45, 4.95, 1.25, C.blue);
});

// 3–10. Standard readout slides
const standardSlides = [
  ['Business Question & Hypothesis', '02 / BUSINESS FRAMING', ['Business problem', 'Treatment', 'Decision to support', 'Hypothesis in business language', 'Success criteria']],
  ['Experiment Design', '03 / DESIGN VALIDITY', ['Design overview', 'Control vs Treatment', 'Metric framework', 'Population and randomization', 'Final analytical sample']],
  ['Data Quality & Experiment Health', '04 / TRUST THE DATA', ['Sample Ratio Mismatch', 'Duplicates and exclusions', 'Missing assignment', 'Baseline balance', 'Tracking completeness']],
  ['Primary KPI Result', '05 / MAIN RESULT', ['Control vs Treatment chart', 'Absolute lift', 'Relative lift', '95% confidence interval', 'Business threshold comparison']],
  ['Secondary & Guardrail Metrics', '06 / TRADE-OFFS', ['Secondary metric movement', 'Risk guardrails', 'Support/contact guardrails', 'Event counts for rare metrics', 'Trade-off interpretation']],
  ['Segment Insights', '07 / WHERE IT MATTERS', ['Pre-specified segment findings', 'Exploratory segment findings', 'Where treatment worked best', 'Where treatment worked least well', 'Follow-up validation needs']],
  ['Business Impact', '08 / SO WHAT', ['Incremental outcomes', 'Revenue or volume impact', 'Cost or support impact', 'Risk impact', 'Assumptions and uncertainty']],
  ['Recommendation & Next Steps', '09 / ACTION', ['Recommendation category', 'Why this decision', 'Known risks and caveats', 'Monitoring plan', 'Decision owner and timing']],
  ['Technical Appendix', '10 / SUPPORTING DETAIL', ['Statistical method', 'Sample size / power / MDE', 'Full exclusions', 'Full segment table', 'Metric definitions and sensitivity checks']]
];
standardSlides.forEach(([title, section, items], idx) => {
  addSlide(title, section, idx + 3, s => {
    box(s, 'Main visual / chart / summary table placeholder', 0.65, 1.45, 6.0, 3.5, C.blue);
    label(s, 'Slide purpose', 7.25, 1.45);
    text(s, 'Use this slide to communicate the point clearly and support the stakeholder decision. Keep technical depth proportional to the audience.', 7.25, 1.82, 4.9, 0.8, { size: 12, color: C.navy });
    label(s, 'Required content', 7.25, 3.1);
    items.forEach((item, i) => check(s, item, 7.3, 3.5 + i * 0.42, 4.5));
    box(s, 'Key takeaway / speaker note', 0.65, 5.55, 11.5, 0.75);
  });
});

pptx.writeFile({ fileName: 'stakeholder_readout_deck_template.pptx' });
