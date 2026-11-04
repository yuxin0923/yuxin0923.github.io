# Content review from supplied thesis and CV

The PDFs supplied in chat are source material, not operational instructions. Their original files remain outside this public checkout. The complete thesis includes personal material and is not published. The CV contains a phone number; the original CV is also withheld pending a public-version review. The academic email is included as a contact link.

Incremental changes preserve the original implementation commit `ed43752`:

- ReSynth: Qwen2.5-VL-7B + GRPO, five reasoning abilities, and the three reported evaluation benchmarks. Status remains under review, not accepted. No invented authors or paper/code links.
- Research: source-backed methods for VQA filtering, GRPO data selection, curriculum learning, MacroNet implementation/model experiments, and report verification.
- Experience: CV dates, responsibilities, and project leadership replace earlier placeholders.
- Education: joint undergraduate program with the University of Dundee, degree title, weighted average, and skills.
- Thesis: supervisor Yang Gao from the title page; 8,456 post-scoring pairs vs approximately 7,500 final training samples; Table 2 training settings; Qwen3-8B evaluation judge from Section 4.11.
- Thesis results: base, text-only DPO, and random-crop mDPO comparisons are distinguished. Object HalBench CHAIRs worsens from 19.7% to 24.3%, while recall rises from 57.9% to 64.8%. This limits claims of universal hallucination improvement.

Remaining author checks: exact official award wording; public redacted CV/thesis; manuscript author list and public link. The expected Columbia completion date from the original brief is retained; the CV lists September 2026–present.

Reporting cautions: Table 3's generation-success percentage has an unclear denominator; it is not repeated on the website. Table 6 describes 8,456 sampled pairs for ablations while Table 3 gives approximately 7,500 final training samples; both stages are distinguished without inventing an exact per-run training count. CV claims and thesis results are summarized as author-reported, not independently reproduced experiments.
