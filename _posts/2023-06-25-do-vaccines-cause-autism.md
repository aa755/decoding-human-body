---
title: "DRAFT: Do vaccines cause autism?"
layout: post
date: 2023-06-25
categories: rant
draft: true
---
## The thin evidence behind the most undebatable medical question: do vaccines cause autism?

Presidential candidate RFK Jr is being censored heavily in mainstream media because whe questions vaccine safety and sometimes almost asserts that vaccines cause autism.
Many vaccine scientists, e.g. Peter Hotez, whose almost every confident claim about Covid was proven incorrect over time, have claimed that the question of whether vaccines cause autism is not even worth debating.
Given their extreme convidence, you would think they have excellent evidence to back up their claims.
In this article, I first critically analyze the evidence they themself put forward to claim that the question is settled science. Then, I critically analyze the evidence of the opposite side.
Although I highly recommend you read the whole article yourself and come to your own conclusions, my takeaway is that the evidence to resolve this question is incredibly weak: many medical scientists would see immediately that the evidence is too weak if the vaccine was a drug, but somehow the word "vaccine" turns off their critical thinking abilities.
Finally, I sketch trials designs that can answer the question of vaccines causing autism or other autoimmune disorders with much more centainty.


Disclaimer: My evidence review is by no means comprehensive: the published medical literature on vaccines is huge. Also, this article is for informational purposes only and does not constitute medical advice.

## evidence review: vaccines dont cause autism
Two of the most vocal vaccine advocates are perhaps Peter Hotez and Paul Offit.
(They both work on vaccine development so they may have some biases due to their conflicts of interest)
Paul Offit published [this paper](https://pubmed.ncbi.nlm.nih.gov/26417097/) which he claims to settle
the question.
Similar evidence has also been used by Peter Hotez. e.g. in his [book](https://books.google.com/books/about/Vaccines_Did_Not_Cause_Rachel_s_Autism.html?id=NkpyDwAAQBAJ) and many other even much more rigorous scientists with apparent no conflicts of interests
to proudly say that they disagree with RFK Jr on childhood vaccines (even though they agree on Covid vaccines and FDA/CDC capture), e.g. [here](https://www.thefp.com/p/what-rfk-jr-gets-rightand-what-he) and [here](https://twitter.com/TracyBethHoeg/status/1670591104654381057).
Below, I consider one by one the evidence they present.

### retrospective observational studies: MMR and autism
There are several studies RETROSPECTIVELY comparing the rates of autism in those who got MMR and those who didn't. Most vaccine evangelists point to these papers first when making the claim that vaccines do not cause autism.
For example, in the section titled "Childhood Vaccines Cause Autism: Got it Wrong", Dr. Vinay Prasad only provides [this paper](https://www.acpjournals.org/doi/10.7326/m18-2101) and a similar earlier paper from 2015 as evidence.
This paper retrospectively looked at "657,461 children born in Denmark from 1999 through 31 December 2010, with follow-up from 1 year of age and through 31 August 2013." and compared the rates of autism among the vaccinated and the unvaccinated children. "Comparing MMR-vaccinated with MMR-unvaccinated children yielded a fully adjusted autism hazard ratio of 0.93 (95% CI, 0.85 to 1.02).". Roughly speaking, they found that an MMR vaccinated child is 0.93 times as likely as a "similar" unvaccinated child to get autism. The 95% confidence interval is mostly
under 1 and barely crosses 1. A confidence interval slightly lower than 95% may be totally below 1.
While this is reassuring, we need to understand the limitations of this study:

#### pitfalls in using retrospective observational studies to prove/disprove causality

It is well known that correlation does not imply causation.
What appears less known among medical scientists is that negative/0 correlation also does not imply lack of causation, even though that [seems obvious to statisticians]().
The reason for both is the same: confounding variables can alter the impact of the variables being tested in *either* direction: they can both increase or decrease the correlation from the causal strength.
The negative correlation seen above may be because of one of the many possibilities (not an exhaustive list):
1. MMR genuinely has nothing to do with autism
2. MMR causes a slight reduction in the chance of autism
3. MMR causes a tiny increase in the chance of autism and some other confounding factors more than cancels out the slight increase. There can be many confounding factors, e.g. children who are vaccinated may have richer parents and their mothers may have had better access to care/adequate-nutrition during pregnancy.
4. MMR causes a massing relative risk reduction in the chance of autism and some other confounding factor cancels out most of that benefit.

Exactly which possibility we are in is hard to determine. The only way that obviously works is to do a randomized trial, where we toss a coin to determine whether someone gets the vaccine or a placebo. In a large trial, randomization can ensure that all confounders are about the same in both vaccine and placebo groups.
All other methods require making a lot of assumptions which are certainly worthy of questioning. For example, reduce the skew due to confounders, observational studies can "adjust" the analysis on various suspected confounding variables to ensure that those suspected confounding factors are roughly the same in the comparisons. While this can help, it can introduce its own problems, especially in retrospective observational studies:

Observational studies can be prospective or retrospective. In prospective studies, ideally, the scientists pre-declare exactly what things they would measure and what are the few hypotheses they are testing. Then they start the study and observe the differences in the future. In retrospective studies, scientists go back and look into historical records to find the differences. Retrospective observational studies bring in their own set of additional pitfalls:

##### p-hacking
Designing an retrospective observational study requires making many, many choices: which source to collect
data from, how to verify the data accuracy, which study subjects to include/exclude, which time period to consider, how to precisely define the variable being measured (e.g. what exactly is considered autism), which suspected confounding factors to adjust. It is often very easy to make these choices to obtain any conclusion you want: often there sets of choices that arrive at completely opposite conclusion.
In RCTs or prospective observational studies, this can be avoided by pre-specifying/publishing the exact trial and analysis protocol *before* staring the trial, an not change it later after seeing how things turn out in the future.
This does not work for retrospective designs because we are looking into the past and there is usually no reliable way to ensure that the trial analysis and protocol was never modified after the researchers saw the data, which typically already existed even before the researchers concieved the trial.

For example, in the above retrospective paper showing a slightly negative correlation between MMR and Covid,
12294 children were excluded from the analyses. To put this in perspective, there were a total 6517 autism diagnoses.
[![missing image. please report to the author](/decoding-human-body/images/autism/excl.jpeg)](https://www.acpjournals.org/na101/home/literatum/publisher/acp/journals/content/aim/2019/aim.2019.170.issue-8/m18-2101/20210930/images/large/m182101ff1_figure_1_study_flow_diagram.jpeg)

Where these exclusions not biased towards vaccinated or unvaccinated? Nobody knows.
Was the exclusion criteria cherry-picked to obtain the conclusion?
Were the variables chosen to adjust cherry-picked to obtain the conclusion?
There are impossible to know for sure in a retrospective design.
One thing I do find odd is that they do not report the unadjusted rates of autism in the vaccinated and the unvaccinated group (number of children in the vaccinated group who got autism vs the number in the unvaccinated group).
I have read hundreds of observational studies, although mostly in nutrition and heart disease drugs, and all of them report both the unadjusted rates and adjusted rates.
One way to mitigate the p-hacking issues is to release the full raw data (after pseudodnymization), so that others can find if there are reasonable analyses that come to the opposite conclusion, but unlike fields like computer science, openness and reproducibility in medical science has a dismal situation.

##### data quality
Often, retrospective studies suffer from the problem of quality of datasets.
In the case of the above study, critics have pointed out that many of the unvaccinated children
may have actually been vaccinated.
They cite apparently credible evidence for this claim: an [article](https://ugeskriftet.dk/dmj/danish-mmr-vaccination-coverage-considerably-higher-reported) from the Danish Medical Journal which dug deeper into a sample of children who were marked unvaccinated in the Danish medical registry that the above study used and found:

> Of the 246 children who were unvaccinated according to the register-based data, 135 (55%) had received vaccination according to the medical records (Table 3).

>The main reason for this discrepancy appeared to be administrative errors in the registration procedure involving the general practice and the region (n = 89, 36%). In 62 of these 89 cases, the GPs stated the correct unique code for performing the MMR1 vaccination, but the invoices were rejected because of errors in the reimbursement request. In the remaining 27 cases, the GPs stated an incorrect unique code or forgot to forward the invoice to the region. The rest of the 135 children with negative vaccination status according to the register-based data, but with positive status according to the medical records, had been vaccinated elsewhere: at another general practice (9%), abroad (8%) or at a hospital (2%).


### other vaccines
Even if MMR does not cause autism -- and I think it does not -- it doesnt mean that the battery of the total ~20 doses infants get together doesnt cause autism. It is not just about magnitude: most other vaccines in today's vaccine schedule work very differently.
MMR is a live virus vaccine: the virus in it infects the human body and replicates just
like any other virus would: it just has been modified/attenuated to not cause the disease that the actual Measles virus may cause in children.
But it is similar enough to the actual measles virus that the antibodies that the body develops against the vaccine version are effective in combating the actual measles virus: very cool technology.
Our bodies have evolved to fight such infections from live/replicating viruses. Decades of research has shown that the human immune system generalizes what it learns from the MMR vaccine and likely also prevent other diseases: these are now called non-specific benefits of vaccines.

Unfortunately, most of the vaccines in use today are not live vaccines.
There is a concern that the virus in a live vaccine can mutate and regain its ability to cause disease: a phenomenon that actually happened with the polio vaccine, although not with MMR and other live vaccines.
Most vaccines today have either the killed virus or just parts (e.g. proteins) of the killed virus: e.g. HepB, IPV, HPV, flu vaccine (not flu mist). The body usually does not know what to do with dead viruses alone and does not mount a good enough immune response
Scientists figured out that by including some some toxin, e.g. aluminium, thimerosal, to kill a small number of cells at the injection site in the muscle, the body can be forced to mount a much better response.
All dead virus vaccines have such adjuvants.
Unfortunately, the same group that showed that live vaccines likely have non-specific beneficial effects ALSO showed that dead virus vaccines likely have non-specific deleterious effects, which we will describe later below.

Most efforts in proving that vaccines do not cause autism has been focused on the MMR vaccines. This is not a
conspiracy but the result of the fact that the first claim about a link between vaccines and autism was made
for the MMR vaccine, by Andrew Wakefield. For other vaccines, we don't even have the low quality evidence that
we have for the MMR vaccine. We only have mechanistic/theoretic evidence and animal trials.
Theories in medicine have a history of being very unreliable in predicting outcomes because we have a very limited understanding of how the human body works.
Animal trials can give some confidence on end-to-end outcomes when done correctly (e.g. in a "good" model, not in an animal specifically designed (e.g. gene knockout) to prove a point: those should just be used to generate hypotheses).
But in this case, they suffer from an easily avoidable problem: they are too underpowered (too small) to detect problems (H/T Chris Masterjohn), yet it is very surprising that experienced scientists like Paul Offit do not see the problem and use this evidence to claim that this is settled science. Below, we discuss the mechanistic/theoretic evidence and animal trials of end-to-end outcomes in more detail.


### mechanistic studies of suspicious components of vaccines

### animal trials of the full vaccine schedule

### human RCTs or lack thereof

### Ending the cat and mouse game: prove safety rather than reacting to safety concerns
Paul Offits laments that the narrative from vaccine safety skeptics has kept on changing:
first they were concerned about MMR, then thermisol, then Aluminium.
When FDA approves a drug, the onus is NOT on the FDA to come up with a mechanism of harm: the onus
is on the drug manufacturer to do multi-year randomized trials to CAUSALLY prove that the drugs have no harms.
Human bodies are extremely complex and we do not know all the process that go in it.
It is impossible to prove safety of anything just going by mechanisms.
Just because some of the mechanisms of harms have been disproven, doesnt mean it is safe.

Perhaps vaccine scientists can learn from my my formal field of research: formal verification (subfield computer science), the field in which I have been working since 2013 (PhD, then postdoc, then industry researcher).
(Obviously, I speak for myself here, not the field).
For a long time, there was a similar cat and mouse game between compiler developers and compiler users claiming that the compiler has bugs.





## evidence review: vaccines cause autism
### observational studies
### aluminium in brains
## evidence of other harms of vaccines
### DTP natural experiment
### atopic dermatitis: schedule vs delayed vaccination

## Trials/Studies to generate better evidence of vaccine safety
first define a very objectice criteria for diagnosing autism
### Prospective studies of vaccinated vs compltetely unvaccinated children
### RCTs of vaccinated vs compltetely unvaccinated children
do we have enough parents who are so much on the fence that they agree to abide by the coin toss?
how large do the trials need to be?

### Trust/Transparency/Verifiability of trial/study results
role of crypto/blockchain/verifiable-voting techniques
