---
title: "Thin Yet Undebatable: Safety Evidence of Childhood Vaccines"
layout: post
date: 2023-06-25
categories: rant
draft: true
---
Many prominent vaccine scientists, e.g. Paul Offit and Peter Hotez, think that the safety of ALL childhood vaccines has been proven so well that no debates should be done about it, and no better-designed trials are needed, [unlike some other medical scientists who specialize in reliability of medical evidence](https://vinayprasadmdmph.substack.com/p/the-only-real-solution-to-vaccine?publication_id=231792&post_id=131012417&isFreemail=false).
Fortunately, now that many people have seen up close how fast the “settled-science” of effectiveness and safety of Covid vaccines changed, more people are questioning the field of vaccine “science” which often behaves more like a religion than science.
Although, I do agree with them that sometimes RFK Jr relies on weak evidence to make claims like vaccines cause harms, I show that those prominent vaccine scientists use similarly weak evidence to make claims of vaccine safety. Also, they cherry pick only the studies that validate their biases with weak evidence and completely ignore even the much stornger evidence that goes against their biases.

First, I review the evidence Paul Offit and Peter Hotez presents to claim that safety of childhood vaccines is settled science.
They both work on vaccine development so they may have some biases due to their conflicts of interest, but people should read their arguments nevertheless.
I focus most of this post on [this paper](https://pubmed.ncbi.nlm.nih.gov/26417097/) in which Paul Offit claims to settle the question. I will first go over the evidence Paul presents. I catergorize the evidence
into 3 categories: obervational studies, animal experiments, randomized controlled trials (gold standard).
For each piece of evidence in each category I discuss their limitations, with concrete examples of how similarly weak evidence have misguided humanity in related fields like nutrition. In many such cases, Paul Offit presented a very biased selection of papers, ignoring the many papers of similar (and sometimes even better) quality on the same subtopic that provide evidence of the opposite.

{% comment %}
I also look at the papers Peter Hotez cited in his [book](https://books.google.com/books/about/Vaccines_Did_Not_Cause_Rachel_s_Autism.html?id=NkpyDwAAQBAJ) about safety of childhood vaccines, and some more recent papers that have been cited by scientists claiming safety of specific childhood vaccines.
{% endcomment %}

## observational studies
There are several studies RETROSPECTIVELY comparing the rates of autism in those who got MMR and those who didn't. Most vaccine evangelists point to these papers first when making the claim that vaccines do not cause autism.
For example, in the section titled "Childhood Vaccines Cause Autism: Got it Wrong", Dr. Vinay Prasad only provides [this paper](https://www.acpjournals.org/doi/10.7326/m18-2101) and a similar earlier paper from 2015 as evidence.
This paper retrospectively looked at "657,461 children born in Denmark from 1999 through 31 December 2010, with follow-up from 1 year of age and through 31 August 2013." and compared the rates of autism among the vaccinated and the unvaccinated children. "Comparing MMR-vaccinated with MMR-unvaccinated children yielded a fully adjusted autism hazard ratio of 0.93 (95% CI, 0.85 to 1.02).". Roughly speaking, they found that an MMR vaccinated child is 0.93 times as likely as a "similar" unvaccinated child to get autism. The 95% confidence interval is mostly
under 1 and barely crosses 1. The interval of confidence slightly lower than 95% may be totally below 1.
While this is somewhat reassuring that the MMR vaccine does not cause autism, we need to understand the limitations of this study:

### observational studies to prove/disprove causality: pitfalls

It is well known that correlation does not imply causation.
What appears less known among medical scientists is that negative/0 correlation also does not imply lack of causation, even though that [seems obvious to statisticians](https://stats.stackexchange.com/questions/221936/does-no-correlation-imply-no-causality).
The reason for both is the same: confounding variables can alter the impact of the variables being tested in *either* direction: they can both increase or decrease the correlation from the causal strength.
My concern is not theoretical: in the field of medical drugs and nutrition, there are many, [many cases](https://chat.openai.com/share/783eb0d4-2cb6-4390-959a-49d7634b4384) where some intervention (e.g. Vitamin E, Hormone Replacement Therapy) was found to be slightly helpful in large observational studies but turned out to be ineffective or even somewhat harmful in large RCTs, which can reliably judge causality. I will summarize those cases and sketch the parallels with the vaccine safety evidence. But first, lets get back to the above MMR study.

The negative correlation seen above may be because of one of the many possibilities (not an exhaustive list):
1. MMR genuinely has nothing to do with autism
2. MMR causes a small reduction in the chance of autism, close to the mean RR of 0.93
2. MMR causes a huge reduction in the chance of autism and some other confounding factor cancels out most of that benefit. A possible confounder could be that people who reject vaccines tend to be "naturalists" and thus also do some other beneficial stuff like reject tylenol ([associated with autism](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9385573/?fc=20210113063650&ff=20220822073638&v=2.17.7), but may or may not be causal) or pesticide-laden food. At least some pesticides have been proven to be harmful after decades of use.
3. MMR causes an increase in the chance of autism and some other confounding factors more than cancels out the slight increase. There can be many confounding factors, e.g. children who are vaccinated may have richer parents and their mothers may have had better access to care/adequate-nutrition during pregnancy. Nutrition, e.g. folate and B12 are known to play an important role in neurodevelopment in the first trimester.

Exactly which possibility we are in is hard to determine. The only way that obviously works is to do a Randomized Controlled Trial (RCT), where we toss a coin to determine whether someone gets the vaccine or a placebo. In a large trial, randomization can ensure that all confounders are about the same in both vaccine and placebo groups.
All other methods require making a lot of assumptions which are certainly worthy of questioning. For example, reduce the skew due to confounders, observational studies can "adjust" the analysis on various suspected confounding variables to ensure that those suspected confounding factors are roughly the same in the comparisons. While this can help, it can introduce its own problems, especially in retrospective observational studies, as we will discuss below.

### How similar quality evidence led us astray: HRT

The current evidence of the safety of the MMR vaccine looks similar to the evidence of the safety of
Hormone Replacement Therapy (HRT) looked like prior to the first RCT about it: large observational studies
*consistently* showed that HRT was associated with fewer cardiovascular events (e.g. heart attacks, strokes).
For example, the Nurses Health Study (NHS) [found](https://pubmed.ncbi.nlm.nih.gov/11119394/) that "the risk for major coronary events was lower among current users of hormone therapy, including short-term users, compared with never-users (relative risk, 0.61 [95% CI, 0.52 to 0.71])".
The negative correlation of HRT with cardiovascular outcomes in NHS was even stronger than the slightly negative correlation of MMR with autism in the above study. Yet, when the Women's Health Initiative did the first Randomized Trial to reliably assess the causality, it was [found](https://jamanetwork.com/journals/jama/fullarticle/195120) to actually increase the risk of not only heart disease but also breast cancer:

>  Estimated hazard ratios (HRs) (nominal 95% confidence intervals [CIs]) were as follows: Coronary Heart Disease, 1.29 (1.02-1.63) with 286 cases; breast cancer, 1.26 (1.00-1.59) with 290 cases; stroke, 1.41 (1.07-1.85) with 212 cases; Pumonary Embolism, 2.13 (1.39-3.25) with 101 cases

If confounders can cause something causing more heart disease to be associated with less heart disease, it can surely cause something more causing autism to be associated with slightly less autism.
Had Cardiologists been as biased as Vaccinologists and declared "settled-science" very prematurely at the consistent negative correleation of HRT with heart disease, many women would have lost their lives to heart disease and breast cancer.

### How similar quality evidence led us astray: Vitamin E for cancer


### Retrospective observational studies: additional pitfalls
Observational studies can be prospective or retrospective. In prospective studies, ideally, the scientists pre-declare exactly what things they would measure and what are the few hypotheses they are testing.
Then they start the study and observe the differences in the future. In retrospective studies, scientists go back and look into historical records to find the differences. Retrospective observational studies bring in their own set of additional pitfalls:
#### P-hacking
Designing an retrospective observational study requires making many, many choices: which source to collect
data from, how to verify the data accuracy, which study subjects to include/exclude, which time period to consider, how to precisely define the variable being measured (e.g. what exactly is considered autism), which suspected confounding factors to adjust. It is often very easy to make these choices to obtain any conclusion you want: often there sets of choices that arrive at completely opposite conclusion.
In RCTs or prospective observational studies, this can be avoided by pre-specifying/publishing the exact trial and analysis protocol *before* staring the trial, an not change it later after seeing how things turn out in the future.
This does not work for retrospective designs because we are looking into the past and there is usually no reliable way to ensure that the trial analysis and protocol was never modified after the researchers saw the data, which typically already existed even before the researchers concieved the trial.

For example, in the above retrospective paper showing a slightly negative correlation between MMR and Covid,
12294 children were excluded from the analyses. To put this in perspective, there were a total 6517 autism diagnoses.
[![missing image. please report to the author](/decoding-human-body/images/autism/excl.jpeg)](https://www.acpjournals.org/na101/home/literatum/publisher/acp/journals/content/aim/2019/aim.2019.170.issue-8/m18-2101/20210930/images/large/m182101ff1_figure_1_study_flow_diagram.jpeg)

Were these exclusions not biased towards vaccinated or unvaccinated? Nobody knows.
Was the exclusion criteria cherry-picked to obtain the conclusion?
Were the variables chosen to adjust cherry-picked to obtain the conclusion?
There are impossible to know for sure in a retrospective design.
One thing I do find odd is that they do not report the unadjusted rates of autism in the vaccinated and the unvaccinated group (number of children in the vaccinated group who got autism vs the number in the unvaccinated group).
I have read hundreds of observational studies, although mostly in nutrition and heart disease drugs, and all of them report both the unadjusted rates and adjusted rates.
One way to mitigate the p-hacking issues is to release the full raw data (after pseudodnymization), so that others can find if there are reasonable analyses that come to the opposite conclusion, but unlike fields like computer science, openness and reproducibility in medical science has a dismal situation.

#### data quality
Often, retrospective studies suffer from the problem of quality of datasets.
In the case of the above study, critics have pointed out that many of the unvaccinated children
may have actually been vaccinated.
They [cite](https://stevekirsch.substack.com/p/key-paper-showing-no-link-between) apparently credible evidence for this claim: an [article](https://ugeskriftet.dk/dmj/danish-mmr-vaccination-coverage-considerably-higher-reported) from the Danish Medical Journal which dug deeper into a sample of children who were marked unvaccinated in the Danish medical registry that the above study used and found:

> Of the 246 children who were unvaccinated according to the register-based data, 135 (55%) had received vaccination according to the medical records (Table 3).

>The main reason for this discrepancy appeared to be administrative errors in the registration procedure involving the general practice and the region (n = 89, 36%). In 62 of these 89 cases, the GPs stated the correct unique code for performing the MMR1 vaccination, but the invoices were rejected because of errors in the reimbursement request. In the remaining 27 cases, the GPs stated an incorrect unique code or forgot to forward the invoice to the region. The rest of the 135 children with negative vaccination status according to the register-based data, but with positive status according to the medical records, had been vaccinated elsewhere: at another general practice (9%), abroad (8%) or at a hospital (2%).


### cherry-picking and double standards: studies associating vaccines with harms
Even if MMR does not cause autism -- and I think it does not -- it doesn't mean that the battery of the total ~20 doses infants get together doesnt cause autism. It is not just about the 20x magnitude: most other vaccines in today's vaccine schedule work very differently.
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
### atopic dermatitis: schedule vs delayed vaccination


## animal trials

### end-to-end outcomes
A little more than a decade ago, RFK Jr asked the question
"why does the CDC ask pregnant women to avoid fish because of mercury content but recommends injecting vaccines containing thimerosal (organic mercury) to them".
The response from vaccine evangelists like Paul Offit [was](https://pauloffit.substack.com/p/my-conversation-with-robert-f-kennedy) that fish contains methyl mercury while vaccines contain ethylmercury (thimerosal) and the latter is much less harmful. He says
> While methylmercury has a half-life in the bloodstream of about 70 days, ethylmercury has a half-life of seven days. So, it’s much less likely to accumulate and do harm.

He cites the [Pichichero](https://pubmed.ncbi.nlm.nih.gov/18245396/)
for the toxicology of ethylmercury, while RFK Jr cites the [Burbacher](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1280342/).
The Pichichero measured mercury in the blood, urine, and feces of human infants receiving thimerosal-containing vaccines at 12 hours to 30 days post injection.
They found that
> The blood mercury half-life was calculated to be 3.7 days and returned to prevaccination levels by day 30.

It is good that at least after 30 days, the blood levels of mercury comes back to prevaccination levels.
It at least says that perhaps after 30 days, the brain is not being exposed to mercury from the bloodtream.
But from that it is impossible to conclude how mercury ended up staying in the brain and what damage, if any, was done in those 30 days.

The Burbacher study, cited by RFK Jr, comes closer to answering those questions: they measured mercury levels in monkey infants at 2, 4, 7, or 28 days after the vaccination with thimerosal-containing vaccines.

### themirosal


Paul Offit quotes the following line from the Burbacher paper:
> no serious medical complications were observed in any of the monkeys.

The monkeys were only observed for 25 days. This is way to short for autism like behaviours to even
begin appearing. But he is right that there is no mention of any brain inflammation being found



flu vaccines are the only vaccines that still have thimerosal. in 1st trimester, they are correlated with autism
https://pubmed.ncbi.nlm.nih.gov/27893896/

this study, which Paul Offit ironically cites for "proving" safety of thermisolxs analyzed data from 3HMOs. in the largest HMO (N=110,833), thermison vaccines were correlated with language delay. in the other 2 HMO's, which were much smaller (n=13K, 16K), no significant correlation was found. They use this inconsistency has evidence of non-causality. but the huge size difference suggests that the other 2 HMOs were rather too small to detect a small effect if there is one.
https://publications.aap.org/pediatrics/article-abstract/112/5/1039/28714/Safety-of-Thimerosal-Containing-Vaccines-A-Two?redirectedFrom=fulltext

Covid mrna vacines have a similar story: first they said never goes into the circulation and remains in muscle and does it job and is gone in a few days.
then when a study showed some mrna in the bloodstream. response: of course a little bit goes into the circulation: nothing to worry about. then some studies show it persists for weeks in some recipients.
then studies seem to implicate it causing myocarditis.


> In fact, studies have shown that EtHg levels in hair are positively correlated with the number of TCV inoculations (Dórea et al. 2011). Although the time-frame between vaccinations allows for a decrease in EtHg levels, this additional mercury source may potentially contribute to aggravate neurotoxic effects in populations already exposed to other Hg sources and species (e.g. consumption of fish with high MeHg) (Dórea, Marques, and Isejima 2012).

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8276940/

> The results indicate that ethylmercury-containing compounds are actively transported across membranes by the L (leucine-preferring)-amino acid transport (LAT) system, the same as methylmercury-containing compounds. Further, 22 studies from 1971 to 2019 show that exposure to ethylmercury-containing compounds (intravenously, intraperitoneally, topically, subcutaneously, intramuscularly, or intranasally administered) results in accumulation of mercury in the brain. In total, these studies indicate that ethylmercury-containing compounds and Thimerosal readily cross the BBB, convert, for the most part, to highly toxic inorganic mercury-containing compounds, which significantly and persistently bind to tissues in the brain, even in the absence of concurrent detectable blood mercury levels

https://www.sciencedirect.com/science/article/abs/pii/S1382668919301875

ethylmercury in hair: https://pubmed.ncbi.nlm.nih.gov/21575620/
### aluminium

## Human RCTs
### Flu vaccines
### Flu vaccines during pregnancy
### DTP natural experiment
### HPV trials


## Downplaying treatments
For very rare disease like tetanus, treatments make much more sense because very few people would need them, thus even if there are some harms, very few people would be affected. Even for non-rare diseases like measles, if there was an effective treatment with slightly more risks than a vaccine, it may be a good tradeoff because many people would not need the treatment: 30% of measles infections are asymptomatic and there appears to be long-term benefits from surviving a mild measles infection: lifelong immunity (unlike MMR) and associated with lower rate of cancer.
### Vitamin A for Measles
Has better quality evidence showing effectiveness (although less effectiveness) than MMR
### Vitamin C for tetanus

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


### Trust/Transparency/Verifiability of trial/study results
role of crypto/blockchain/verifiable-voting techniques
