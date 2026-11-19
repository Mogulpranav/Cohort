# Agent vs TREC disagreements: 2021

# TREC says ELIGIBLE, agent says EXCLUDED (good trial pushed down): 7 cases

---

## Patient 1 | NCT00003537

**Trial:** Antineoplaston Therapy in Treating Adult Patients With Anaplastic Astrocytoma

**Agent reason:** The patient has received prior myelosuppressive chemotherapy, which is an exclusion criterion.

**Criteria the agent marked FAIL:**

- (exclusion) No prior myelosuppressive chemotherapy
  - evidence: "11 cycles of temozolomide 7 days on and 7 days off. This was followed by CPT-11 Weekly x4"
  - reasoning: Both temozolomide and CPT-11 (irinotecan) are myelosuppressive agents, violating the exclusion of prior myelosuppressive chemotherapy.

<details><summary>Patient note</summary>

Patient is a 45-year-old man with a history of anaplastic astrocytoma of the spine complicated by severe lower extremity weakness and urinary retention s/p Foley catheter, high-dose steroids, hypertension, and chronic pain. The tumor is located in the T-L spine, unresectable anaplastic astrocytoma s/p radiation. Complicated by progressive lower extremity weakness and urinary retention. Patient initially presented with RLE weakness where his right knee gave out with difficulty walking and right anterior thigh numbness. MRI showed a spinal cord conus mass which was biopsied and found to be anaplastic astrocytoma. Therapy included field radiation t10-l1 followed by 11 cycles of temozolomide 7 days on and 7 days off. This was followed by CPT-11 Weekly x4 with Avastin Q2 weeks/ 2 weeks rest and repeat cycle.

</details>

<details><summary>Full eligibility criteria</summary>

```
DISEASE CHARACTERISTICS:

          -  Histologically or cytologically confirmed diagnosis of anaplastic astrocytoma

          -  Tumor subtotally resected or biopsied prior to therapy

          -  Evidence of residual tumor by MRI scan performed within two weeks prior to study entry

          -  No brain stem tumors

        PATIENT CHARACTERISTICS:

        Age:

          -  18 and over

        Performance status:

          -  Karnofsky 60-100%

        Life expectancy:

          -  More than 2 months

        Hematopoietic:

          -  WBC at least 1,500/mm^3

          -  Platelet count at least 50,000/mm^3

          -  Hemoglobin at least 10 g/dL

        Hepatic:

          -  Bilirubin no greater than 2.5 mg/dL

          -  SGOT and SGPT no greater than 5 times upper limit of normal

          -  No hepatic failure

        Renal:

          -  Creatinine no greater than 2.5 mg/dL

          -  No renal failure

        Cardiovascular:

          -  No prior congestive heart failure

          -  No coronary artery disease

          -  No myocardial infarction within the past year

          -  No angina requiring medication

          -  No uncontrolled hypertension

        Pulmonary:

          -  No moderate to severe chronic obstructive pulmonary disease

        Other:

          -  Not pregnant or nursing

          -  Fertile patients must use effective contraception during and for 4 weeks after study
             participation

          -  No active infection

          -  No other concurrent serious disease

          -  No other prior malignancy except carcinoma in situ of the cervix or superficial
             nonmelanoma skin cancer

        PRIOR CONCURRENT THERAPY:

        Biologic therapy:

          -  No prior immunotherapy

          -  No concurrent immunomodulating agents

        Chemotherapy:

          -  No prior myelosuppressive chemotherapy

        Endocrine therapy:

          -  Concurrent corticosteroids for cerebral edema allowed

        Radiotherapy:

          -  No prior myelosuppressive radiotherapy

          -  No concurrent radiotherapy

        Surgery:

          -  See Disease Characteristics

          -  Recovered from any prior surgery

        Other:

          -  No prior cytodifferentiating agents

          -  No prior antineoplaston therapy

          -  No other concurrent antineoplastic agents
```

</details>

**Who is right?** (mark one)
- [ ] Agent wrong: misread the note or the criterion
- [ ] Agent too strict: e.g. ignored a time window ("within 4 weeks") or a "unless" clause
- [ ] Label looks wrong (like the CPT-11 case)
- [ ] Unclear / needs more info

Notes:

---

## Patient 1 | NCT00003621

**Trial:** Combination Chemotherapy Plus Radiation Therapy in Treating Patients With Anaplastic Astrocytoma

**Agent reason:** The patient fails key eligibility rules (newly diagnosed requirement and required ≥5‑year intervals since prior chemotherapy and radiotherapy).

**Criteria the agent marked FAIL:**

- (inclusion) Newly diagnosed anaplastic astrocytoma
  - evidence: "Therapy included field radiation t10-l1 followed by 11 cycles of temozolomide ... This was followed by CPT-11 Weekly x4 with Avastin"
  - reasoning: The patient has already received radiation and multiple chemotherapy cycles, indicating the disease is not newly diagnosed.
- (exclusion) At least 5 years since prior chemotherapy
  - evidence: "11 cycles of temozolomide ... followed by CPT-11 Weekly x4 with Avastin"
  - reasoning: Chemotherapy was administered recently, far less than the required 5‑year interval.
- (exclusion) At least 5 years since prior radiotherapy
  - evidence: "field radiation t10-l1"
  - reasoning: Radiation therapy was given recently, not meeting the 5‑year washout period.

<details><summary>Patient note</summary>

Patient is a 45-year-old man with a history of anaplastic astrocytoma of the spine complicated by severe lower extremity weakness and urinary retention s/p Foley catheter, high-dose steroids, hypertension, and chronic pain. The tumor is located in the T-L spine, unresectable anaplastic astrocytoma s/p radiation. Complicated by progressive lower extremity weakness and urinary retention. Patient initially presented with RLE weakness where his right knee gave out with difficulty walking and right anterior thigh numbness. MRI showed a spinal cord conus mass which was biopsied and found to be anaplastic astrocytoma. Therapy included field radiation t10-l1 followed by 11 cycles of temozolomide 7 days on and 7 days off. This was followed by CPT-11 Weekly x4 with Avastin Q2 weeks/ 2 weeks rest and repeat cycle.

</details>

<details><summary>Full eligibility criteria</summary>

```
DISEASE CHARACTERISTICS: Histologically confirmed, newly diagnosed, anaplastic astrocytoma
        No oligodendrogliomas or oligoastrocytomas

        PATIENT CHARACTERISTICS: Age: 18 and over Performance status: ECOG 0-2 Life expectancy: Not
        specified Hematopoietic: WBC at least 3500/mm3 Platelet count at least 130,000/mm3 Hepatic:
        Bilirubin no greater than 1.5 times upper limit of normal (ULN) SGOT no greater than 2
        times ULN Renal: Creatinine no greater than 0.5 mg/dL Other: Not pregnant or nursing
        Fertile patients must use effective contraception No uncontrolled infection No concurrent
        malignant disease or major medical problem except superficial skin cancers

        PRIOR CONCURRENT THERAPY: Biologic therapy: Not specified Chemotherapy: At least 5 years
        since prior chemotherapy Endocrine therapy: Concurrent corticosteroids allowed
        Radiotherapy: At least 5 years since prior radiotherapy Surgery: Not specified
```

</details>

**Who is right?** (mark one)
- [ ] Agent wrong: misread the note or the criterion
- [ ] Agent too strict: e.g. ignored a time window ("within 4 weeks") or a "unless" clause
- [ ] Label looks wrong (like the CPT-11 case)
- [ ] Unclear / needs more info

Notes:

---

## Patient 2 | NCT03635424

**Trial:** Medtronic Transcatheter Aortic Valve Replacement (TAVR) Low Risk Bicuspid Study

**Agent reason:** Patient is under the minimum age requirement (48 years < 60).

**Criteria the agent marked FAIL:**

- (exclusion) Age less than 60 years
  - evidence: "48 M"
  - reasoning: Patient is 48, which is below the minimum age of 60.

<details><summary>Patient note</summary>

48 M with a h/o HTN hyperlipidemia, bicuspid aortic valve, and tobacco abuse who presented to his cardiologist on [**2148-10-1**] with progressive SOB and LE edema. TTE revealed severe aortic stenosis with worsening LV function. EF was 25%. RV pressure was 41 and had biatrial enlargement. Noted to have 2+ aortic insufficiency with mild MR. He was sent home from cardiology clinic with Lasix and BB (which he did not tolerate), continued to have worsening SOB and LE edema and finally presented here for evaluation.
During this admission repeat echo confirmed critical aortic stenosis showing left ventricular hypertrophy with cavity dilation and severe global hypokinesis, severe aortic valve stenosis with underlying bicuspid aortic valve, dilated ascending aorta, mild pulmonary artery systolic hypertension. The patient underwent a preop workup for valvular replacement with preop chest CT scan and carotid US (showing moderate heterogeneous plaque with bilateral 1-39% ICA stenosis). He also underwent a cardiac cath with right heart cath to evaluate his pulm art pressures which showed no angiographically apparent flow-limiting coronary artery disease.

</details>

<details><summary>Full eligibility criteria</summary>

```
Inclusion Criteria:

          1. Severe aortic stenosis, defined as follows:

               1. For symptomatic patients:

                  Aortic valve area ≤1.0 cm2 (or aortic valve area index of ≤0.6 cm2/m2), OR mean
                  gradient ≥40 mmHg, OR Maximal aortic valve velocity ≥4.0 m/sec by transthoracic
                  echocardiography at rest

               2. For asymptomatic patients:

             Very severe aortic stenosis with an aortic valve area of ≤1.0 cm2 (or aortic valve
             area index of ≤0.6 cm2/m2), AND maximal aortic velocity ≥5.0 m/sec, or mean gradient
             ≥60 mmHg by transthoracic echocardiography at rest, OR

             Aortic valve area of ≤1.0 cm2 (or aortic valve area index of ≤0.6 cm2/m2), AND a mean
             gradient ≥40 mmHg or maximal aortic valve velocity ≥4.0 m/sec by transthoracic
             echocardiography at rest, AND an exercise tolerance test that demonstrates a limited
             exercise capacity, abnormal BP response, or arrhythmia OR

             Aortic valve area of ≤1.0 cm2 (or aortic valve area index of ≤0.6 cm2/m2), AND mean
             gradient ≥40 mmHg, or maximal aortic valve velocity ≥4.0 m/sec by transthoracic
             echocardiography at rest, AND a left ventricular ejection fraction <50%.

          2. Patient is considered low risk for SAVR, where low risk is defined as predicted risk
             of mortality for SAVR <3% at 30 days per multidisciplinary local heart team
             assessment.

          3. Bicuspid aortic valve anatomy (all sub-types) confirmed by MDCT.

          4. The subject and the treating physician agree that the subject will return for all
             required post-procedure follow-up visits.

        Exclusion Criteria:

          1. Any condition considered a contraindication for placement of a bioprosthetic valve
             (eg, subject is indicated for mechanical prosthetic valve).

          2. Age less than 60 years

          3. A known hypersensitivity or contraindication to any of the following that cannot be
             adequately pre-medicated:

               1. aspirin or heparin (HIT/HITTS) and bivalirudin

               2. ticlopidine and clopidogrel

               3. Nitinol (titanium or nickel)

               4. contrast media

          4. Blood dyscrasias as defined: leukopenia (WBC <1000 mm3), thrombocytopenia (platelet
             count <50,000 cells/mm3), history of bleeding diathesis or coagulopathy, or
             hypercoagulable states.

          5. Ongoing sepsis, including active endocarditis.

          6. Any percutaneous coronary or peripheral interventional procedure with a bare metal
             stent or drug eluting stent performed within 30 days prior to screening committee
             approval.

          7. Multivessel coronary artery disease with a Syntax score >22 and/or unprotected left
             main coronary artery.

          8. Symptomatic carotid or vertebral artery disease or successful treatment of carotid
             stenosis within 10 weeks of Heart Team assessment.

          9. Cardiogenic shock manifested by low cardiac output, vasopressor dependence, or
             mechanical hemodynamic support.

         10. Recent (within 2 months of Heart Team assessment) cerebrovascular accident (CVA) or
             transient ischemic attack (TIA).

         11. Gastrointestinal (GI) bleeding that would preclude anticoagulation.

         12. Subject refuses a blood transfusion.

         13. Severe dementia (resulting in either inability to provide informed consent for the
             study/procedure, prevents independent lifestyle outside of a chronic care facility, or
             will fundamentally complicate rehabilitation from the procedure or compliance with
             follow-up visits).

         14. Estimated life expectancy of less than 24 months due to associated non-cardiac
             co-morbid conditions.

         15. Other medical, social, or psychological conditions that in the opinion of the
             investigator precludes the subject from appropriate consent or adherence to the
             protocol required follow-up exams.

         16. Currently participating in an investigational drug or another device study (excluding
             registries).

         17. Evidence of an acute myocardial infarction ≤30 days before the study procedure due to
             unstable coronary artery disease (WHO criteria).

         18. Need for emergency surgery for any reason.

         19. Subject is pregnant or breast feeding.

         20. Subject is legally incompetent, or otherwise vulnerable

             Anatomical exclusion criteria:

         21. Pre-existing prosthetic heart valve in any position.

         22. Severe mitral regurgitation amenable to surgical replacement or repair.

         23. Severe tricuspid regurgitation amenable to surgical replacement or repair.

         24. Moderate or severe mitral stenosis amenable to surgical replacement or repair.

         25. Hypertrophic obstructive cardiomyopathy with left ventricular outflow gradient.

         26. Prohibitive left ventricular outflow tract calcification.

         27. Sinus of Valsalva diameter unsuitable for placement of the self-expanding
             bioprosthesis

         28. Aortic annulus diameter of <18 or >30 mm.

         29. Significant ascending aortopathy requiring surgical repair

         30. Ascending aorta diameter > 4.5 cm

             For transfemoral or transaxillary (subclavian) access:

         31. Access vessel mean diameter <5.0 mm for Evolut 23R, 26R, or 29R mm TAV, or access
             vessel mean diameter <5.5 mm for Evolut 34R mm or Evolut PRO 23R, 26R, 29 R mm TAV.
             However, for transaxillary (subclavian) access in patients with a patent LIMA, access
             vessel mean diameter <5.5mm for Evolut 23R, 26R, or 29R mm TAV, or access vessel mean
             diameter <6.0 mm for the Evolut 34R or Evolut PRO TAV.
```

</details>

**Who is right?** (mark one)
- [ ] Agent wrong: misread the note or the criterion
- [ ] Agent too strict: e.g. ignored a time window ("within 4 weeks") or a "unless" clause
- [ ] Label looks wrong (like the CPT-11 case)
- [ ] Unclear / needs more info

Notes:

---

## Patient 6 | NCT01309750

**Trial:** Small Bowel Transit Time in Clostridium Difficile Colitis

**Agent reason:** The patient is on vasoactive pressors, which fails an exclusion criterion.

**Criteria the agent marked FAIL:**

- (exclusion) hypotension requiring vasoactive agents
  - evidence: "septic on pressors (levophed)"
  - reasoning: The patient required pressor support, indicating hypotension that meets this exclusion.

<details><summary>Patient note</summary>

Patient is a 55yo woman with h/o ESRD on HD and peritoneal dialysis who presented with watery, non bloody diarrhea and weakness. She has a history of 2 prior C diff infections, the most recent just 1 month ago. Recent antibx use in the last month on prior admission. Was also txd for Cdiff at that time for 14 d. course with po vanco. Pt was initially admitted to the ICU and was septic on pressors (levophed) until the morning of [**8-26**] with leukocytosis but no fever. C diff assay positive on admission, and pt had leukocytosis consistent with C diff. Patient was placed on Vanco po, Flagyl IV and Flagyl po initially, and when patient improved she was transitioned to Vanco oral and Flagyl oral on [**8-29**]. Patient was treated with Vanco for an extended course of 6 weeks given her recurrent C diff. Pt was also encouraged to take probiotics and to bleach her home when she was discharged.

</details>

<details><summary>Full eligibility criteria</summary>

```
Inclusion Criteria:

          -  ICU patient

          -  positive c. diff PCR or visualization of pseudomembranes on colonoscopy

          -  able to give consent or have representative to give consent

          -  ability to drink contrast or have a previously placed nasogastric tube

          -  approval from the intensivist on duty/ICU Attending physician

        Exclusion Criteria:

          -  Under age 18

          -  pregnant

          -  need for gastric motility medications

          -  need for anti-diarrheal medication

          -  need for surgery

          -  previous small bowel or gastric surgery

          -  inability to drink nuclear tracer without nasogastric tube in place

          -  hypotension requiring vasoactive agents

          -  APACHE II score greater than 30
```

</details>

**Who is right?** (mark one)
- [ ] Agent wrong: misread the note or the criterion
- [ ] Agent too strict: e.g. ignored a time window ("within 4 weeks") or a "unless" clause
- [ ] Label looks wrong (like the CPT-11 case)
- [ ] Unclear / needs more info

Notes:

---

## Patient 6 | NCT01346059

**Trial:** Intracolonic Vancomycin Therapy in Severe C. Diff Colitis

**Agent reason:** Patient fails exclusion criteria (use of probiotics and concurrent anti‑C. difficile antibiotics).

**Criteria the agent marked FAIL:**

- (exclusion) need for probiotics
  - evidence: "Pt was also encouraged to take probiotics"
  - reasoning: The patient is being advised to take probiotics, which is an excluded condition.
- (exclusion) need for other medications with action against C. diff.
  - evidence: "Patient was placed on Vanco po, Flagyl IV and Flagyl po initially, and when patient improved she was transitioned to Vanco oral and Flagyl oral... treated with Vanco for an extended course of 6 weeks"
  - reasoning: The patient is receiving vancomycin and metronidazole, both active against C. difficile, which is excluded.

<details><summary>Patient note</summary>

Patient is a 55yo woman with h/o ESRD on HD and peritoneal dialysis who presented with watery, non bloody diarrhea and weakness. She has a history of 2 prior C diff infections, the most recent just 1 month ago. Recent antibx use in the last month on prior admission. Was also txd for Cdiff at that time for 14 d. course with po vanco. Pt was initially admitted to the ICU and was septic on pressors (levophed) until the morning of [**8-26**] with leukocytosis but no fever. C diff assay positive on admission, and pt had leukocytosis consistent with C diff. Patient was placed on Vanco po, Flagyl IV and Flagyl po initially, and when patient improved she was transitioned to Vanco oral and Flagyl oral on [**8-29**]. Patient was treated with Vanco for an extended course of 6 weeks given her recurrent C diff. Pt was also encouraged to take probiotics and to bleach her home when she was discharged.

</details>

<details><summary>Full eligibility criteria</summary>

```
Inclusion Criteria:

          -  SICU patient

          -  positive c. diff toxin assay

          -  visualization of pseudomembranes on colonoscopy,

          -  able to give consent or have representative to give consent.

        Exclusion Criteria:

          -  Under age 18

          -  pregnant

          -  absence of a colon or surgical discontinuity of bowel

          -  allergy to vancomycin

          -  need for anti-diarrheal medication

          -  need for prolonged antibiotics for other cause

          -  need for probiotics

          -  need for other medications with action against C. diff.

          -  need for surgery, colon perforation

          -  recent IV IG use

          -  toxic megacolon.
```

</details>

**Who is right?** (mark one)
- [ ] Agent wrong: misread the note or the criterion
- [ ] Agent too strict: e.g. ignored a time window ("within 4 weeks") or a "unless" clause
- [ ] Label looks wrong (like the CPT-11 case)
- [ ] Unclear / needs more info

Notes:

---

## Patient 6 | NCT01570634

**Trial:** Proof-of-Concept, Calcium Aluminosilicate Anti-Diarrheal (CASAD) for Treatment of Clostridium Difficile Infection

**Agent reason:** The patient fails two exclusion criteria: septic shock requiring pressors and excessive (>5) doses of oral vancomycin.

**Criteria the agent marked FAIL:**

- (exclusion) Patients with hypotension (systolic blood pressure < 90 mm Hg) or septic shock requiring pressors
  - evidence: "patient was initially admitted to the ICU and was septic on pressors (levophed)"
  - reasoning: The patient required vasopressor support for septic shock, which meets this exclusion.
- (exclusion) More than 5 doses of metronidazole or oral vancomycin prior to starting on study drug for the current C. difficile diagnosis
  - evidence: "Patient was treated with Vanco for an extended course of 6 weeks"
  - reasoning: An extended 6‑week oral vancomycin course far exceeds five doses, triggering this exclusion.

<details><summary>Patient note</summary>

Patient is a 55yo woman with h/o ESRD on HD and peritoneal dialysis who presented with watery, non bloody diarrhea and weakness. She has a history of 2 prior C diff infections, the most recent just 1 month ago. Recent antibx use in the last month on prior admission. Was also txd for Cdiff at that time for 14 d. course with po vanco. Pt was initially admitted to the ICU and was septic on pressors (levophed) until the morning of [**8-26**] with leukocytosis but no fever. C diff assay positive on admission, and pt had leukocytosis consistent with C diff. Patient was placed on Vanco po, Flagyl IV and Flagyl po initially, and when patient improved she was transitioned to Vanco oral and Flagyl oral on [**8-29**]. Patient was treated with Vanco for an extended course of 6 weeks given her recurrent C diff. Pt was also encouraged to take probiotics and to bleach her home when she was discharged.

</details>

<details><summary>Full eligibility criteria</summary>

```
Inclusion Criteria:

          -  C. difficile-associated diarrhea at the time of enrollment

          -  18 years old and up

          -  Ability to take oral medications

          -  Negative urine pregnancy test for women of childbearing age

          -  Must have the ability to understand and the willingness to provide a written informed
             consent to participate in the study

        Exclusion Criteria:

          -  History of known allergy to silicates

          -  Patients with signs of toxic megacolon, peritonitis, pseudomembranous colitis or bowel
             perforation

          -  Patients with hypotension (systolic blood pressure < 90 mm Hg) or septic shock
             requiring pressors

          -  Patients with other known causes of diarrhea or colitis

          -  Pregnancy or lactation

          -  History of significant neurological or psychiatric disorders that would impede giving
             consent, treatment, or follow up

          -  Participation in any other study where the subject is actively taking investigational
             medication within the last 30 days

          -  More than 5 doses of metronidazole or oral vancomycin prior to starting on study drug
             for the current C. difficile diagnosis. Administration of metronidazole or oral
             vancomycin for treatment of prior C. difficile diagnosis is not exclusionary as some
             patients may be experiencing a relapse of C. difficile.

          -  Any other antibiotic, toxin-binding agent or fecal transplant used for the treatment
             of C. difficile prior to or added to the subject's standard-of-care treatment regimen.
             Use of intravenous vancomycin is not exclusionary.
```

</details>

**Who is right?** (mark one)
- [ ] Agent wrong: misread the note or the criterion
- [ ] Agent too strict: e.g. ignored a time window ("within 4 weeks") or a "unless" clause
- [ ] Label looks wrong (like the CPT-11 case)
- [ ] Unclear / needs more info

Notes:

---

## Patient 6 | NCT04781387

**Trial:** Evaluation of CRS3123 vs. Oral Vancomycin in Adult Patients With Clostridioides Difficile Infection

**Agent reason:** The patient has had more than one recurrence of C. difficile infection, which does not meet the inclusion criterion limiting eligibility to a primary episode or first recurrence.

**Criteria the agent marked FAIL:**

- (inclusion) Participants with a primary episode or first recurrence of CDI are eligible
  - evidence: "history of 2 prior C diff infections, the most recent just 1 month ago"
  - reasoning: The patient has had two prior infections, indicating a second recurrence, which exceeds the allowed primary episode or first recurrence.

<details><summary>Patient note</summary>

Patient is a 55yo woman with h/o ESRD on HD and peritoneal dialysis who presented with watery, non bloody diarrhea and weakness. She has a history of 2 prior C diff infections, the most recent just 1 month ago. Recent antibx use in the last month on prior admission. Was also txd for Cdiff at that time for 14 d. course with po vanco. Pt was initially admitted to the ICU and was septic on pressors (levophed) until the morning of [**8-26**] with leukocytosis but no fever. C diff assay positive on admission, and pt had leukocytosis consistent with C diff. Patient was placed on Vanco po, Flagyl IV and Flagyl po initially, and when patient improved she was transitioned to Vanco oral and Flagyl oral on [**8-29**]. Patient was treated with Vanco for an extended course of 6 weeks given her recurrent C diff. Pt was also encouraged to take probiotics and to bleach her home when she was discharged.

</details>

<details><summary>Full eligibility criteria</summary>

```
1. More than or equal to 3 diarrheal stools/day in 24 hours prior to randomization and in
             the judgment of the investigator that C difficile is the likely causative agent for
             the diarrhea.

          2. Stool positive for C. difficile GDH plus Toxin A and/or B

          3. Participants with a primary episode or first recurrence of CDI are eligible

          4. In the judgement of the investigator, the expectation that the participant will
             survive with effective antibiotic therapy and appropriate supportive care for the
             anticipated duration of the study

          5. Participants may be either inpatient or outpatient
```

</details>

**Who is right?** (mark one)
- [ ] Agent wrong: misread the note or the criterion
- [ ] Agent too strict: e.g. ignored a time window ("within 4 weeks") or a "unless" clause
- [ ] Label looks wrong (like the CPT-11 case)
- [ ] Unclear / needs more info

Notes:

# TREC says EXCLUDED, agent says ELIGIBLE (missed an exclusion): 6 cases

---

## Patient 5 | NCT02089217

**Trial:** Carotid Revascularization and Medical Management for Asymptomatic Carotid Stenosis Trial

**Agent reason:** Patient meets all applicable inclusion criteria and has no exclusion criteria that are violated.

<details><summary>Patient note</summary>

74M hx of CAD s/p CABG, EF 60% prior CVA (no residual deficits), HTN, HL, DMII, Moderate to Severe PVD was referred to cardiology for evaluation of PVD, and on examination patient was found to have carotid bruits. Upon further review of symptoms the pt reports + Occasional dizziness, no prior syncope occasional HA, Denies CP/SOB. No sensory or motor defects. He recalls that he might have had a stroke 10-15 years ago without any residual deficit. Prior to CABG he only had diaphoresis.
Further review of systems is notable for absence of chest pain, dyspnea on exertion, paroxysmal nocturnal dyspnea, orthopnea, palpitations, syncope or presyncope. He underwent Carotid U/S that showed significant bilateral carotid stenosis, L>R. Angiography revealed an 80% stenosis of the R ICA and a 90% L ICA stenosis. Cerebral angiography further revealed patent right ACA and MCA and patent left ACA and left MCA.
Past Medical History:
CAD s/p CABG in [**2154**] ([**Hospital1 112**])
Prior CVA
Bilateral carotid artery disease
Anemia
PVD
Hypertension
Diabetes c/b retinopathy and peripheral neuropathy
Cataracts s/p surgery
Thyroid nodule
Colon polyps s/p resection
Intermittent Lower back pain
Proteinuria
s/p right elbow fracture as a child
Arthritis

</details>

<details><summary>Full eligibility criteria</summary>

```
General Inclusion Criteria

          1. Patients ≥35 years old.

          2. Carotid stenosis defined as:

               -  Stenosis ≥70% by catheter angiography (NASCET Criteria); OR

               -  by DUS with ≥70% stenosis defined by a peak systolic velocity of at least 230
                  cm/s plus at least one of the following:

                    1. an end diastolic velocity ≥100 cm/s, or

                    2. internal carotid/common carotid artery peak systolic velocity ratio ≥4.0, or

                    3. CTA with ≥ 70% stenosis, or

                    4. MRA with ≥ 70% stenosis.

          3. No medical history of stroke or TIA ipsilateral to the stenosis within 180 days of
             randomization. Life-long asymptomatic patients will be defined as having no medical
             history of stroke or transient ischemic attack and negative responses to all of the
             symptom items on the Questionnaire for Verifying Stroke-free Status (QVSS).18

          4. Patients must have a modified Rankin Scale score of 0 or 1 at the time of informed
             consent.

          5. Women must not be of childbearing potential or, if of childbearing potential, have a
             negative pregnancy test prior to randomization.

          6. Patients must agree to comply with all protocol-specified follow-up appointments.

          7. Patients must sign a consent form that has been approved by the local governing
             Institutional Review Board (IRB)/Medical Ethics Committee (MEC) of the respective
             clinical site.

          8. Randomization to treatment group will apply to only one carotid artery for patients
             with bilateral carotid stenosis. Management of the non-randomized stenosis may be done
             in accordance with local PI recommendation. Treatment of the non-study internal
             carotid artery must take place at least 30 days prior to randomization, or greater
             than 44 days after randomization and 30 days after the study procedure is completed
             (whichever is longer).

          9. Carotid stenosis must be treatable with CEA, CAS, or either procedure.

        General Exclusion Criteria

          1. Intolerance or allergic reaction to a study medication without a suitable management
             alternative.

          2. GI hemorrhage within 1 month prior to enrollment that would preclude antiplatelet
             therapy.

          3. Prior major ipsilateral stroke in the past with substantial residual disability (mRS ≥
             2) that is likely to confound study outcomes.

          4. Severe dementia.

          5. History of major symptomatic intracranial hemorrhage within 12 months that was not
             related to anticoagulation.

          6. Prior Intracranial hemorrhage that the investigator believes represents a
             contraindication to the perioperative or periprocedural antithrombotic and
             antiplatelet treatments necessary to complete endarterectomy or stenting per protocol.

          7. Current neurologic illness characterized by fleeting or fixed neurologic deficits that
             cannot be distinguished from TIA or stroke.

          8. Patient objects to future blood transfusions.

          9. Platelet count <100,000/microliter or history of heparin-induced thrombocytopenia.

         10. Anticoagulation with Phenprocoumon (Marcumar®), warfarin, or a direct thrombin
             inhibitor, or anti-Xa agents.

         11. Chronic atrial fibrillation.

         12. Any episode of atrial fibrillation within the past 6 months or history of paroxysmal
             atrial fibrillation that is deemed to require chronic anticoagulation.

         13. Other high-risk cardiac sources of emboli, including left ventricular aneurysm, severe
             cardiomyopathy, aortic or mitral mechanical heart valve, severe calcific aortic
             stenosis (valve area < 1.0 cm2), endocarditis, moderate to severe mitral stenosis,
             left atrial thrombus, or any intracardiac mass, or known unrepaired PFO with prior
             paradoxical embolism.

         14. Unstable angina defined as rest angina with ECG changes that is not amenable to
             revascularization (patients should undergo planned coronary revascularization at least
             30 days before randomization).

         15. Left Ventricular Ejection fraction <30% or admission for heart failure in prior 6
             months.

         16. Respiratory insufficiency with life expectancy < 4 years or FEV1 <30% of predicted
             value.

         17. Known malignancy other than basal cell non-melanoma skin cancer. There are two
             exceptions to this rule: patients with prior cancer treatment and no recurrence for >5
             years are eligible for enrollment and cancer patients with life expectancy of greater
             than 5 years are eligible for enrollment.

         18. Any major surgery, major trauma, revascularization procedure, or acute coronary
             syndrome within the past 1 month.

         19. Either the serum creatinine is ≥ 2.5 mg/dl or the estimated GFR is < 30 cc/min.

         20. Major (non-carotid) surgery/procedures planned within 3 months after enrollment.

         21. Currently listed or being evaluated for major organ transplantation (i.e. heart, lung,
             liver, kidney).

         22. Actively participating in another drug or aortic arch or cerebrovascular device trial
             for which participation in CREST-2 would be compromised with regard to follow-up
             assessment of outcomes or continuation in CREST-2.

         23. Inability to understand and cooperate with study procedures or provide informed
             consent.

         24. Non-atherosclerotic carotid stenosis (dissection, fibromuscular dysplasia, or stenosis
             following radiation therapy).

         25. Previous ipsilateral CEA or CAS.

         26. Ipsilateral internal or common carotid artery occlusion.

         27. Intra-carotid floating thrombus.

         28. Ipsilateral intracranial aneurysm > 5 mm.

         29. Extreme morbid obesity that would compromise patient safety during the procedure or
             would compromise patient safety during the periprocedural period.

         30. Coronary artery disease with two or more proximal or major diseased coronary arteries
             with 70% stenosis that have not, or cannot, be revascularized.

        Specific carotid endarterectomy exclusion criteria

        Patients who are being considered for revascularization by CEA must not have any of the
        following criteria:

          1. Serious adverse reaction to anesthesia not able to be overcome by pre-medication.

          2. Distal/intracranial stenosis greater than index lesion.

          3. Any of the following anatomical: radical neck dissection; surgically inaccessible
             lesions (e.g. above cervical spine level 2 (C2)); adverse neck anatomy that limits
             surgical exposure (e.g. spinal immobility - inability to flex neck beyond neutral or
             kyphotic deformity, or short obese neck); presence of tracheostomy stoma; laryngeal
             nerve palsy contralateral to target vessel; or previous extracranial-intracranial or
             subclavian bypass procedure ipsilateral to the target vessel.

        Specific Carotid Artery Stenting Exclusion Criteria

        Patients who are being considered for revascularization by CAS must not have any of the
        following criteria:

          1. Allergy to intravascular contrast dye not amenable to pre-medication.

          2. Type III, aortic arch anatomy.

          3. Angulation or tortuosity (≥ 90 degree) of the innominate and common carotid artery
             that precludes safe, expeditious sheath placement or that will transmit a severe loop
             to the internal carotid after sheath placement.

          4. Severe angulation or tortuosity of the internal carotid artery (including calyceal
             origin from the carotid bifurcation) that precludes safe deployment of embolic
             protection device or stent. Severe tortuosity is defined as 2 or more ≥ 90 degree
             angles within 4 cm of the target stenosis.

          5. Proximal/ostial CCA, innominate stenosis or distal/intracranial stenosis greater than
             index lesion.

             Excessive circumferential calcification of the stenotic lesion defined as >3mm
             thickness of calcification seen in orthogonal views on fluoroscopy.(Note: Anatomic
             considerations such as tortuosity, arch anatomy, and calcification must be evaluated
             even more carefully in elderly subjects (≥ 70 years).)

          6. Target ICA vessel reference diameter <4.0 mm or >9.0 mm. Target ICA measurements may
             be made from angiography of the contralateral artery. The reference diameter must be
             appropriate for the devices to be used.

          7. Inability to deploy or utilize an FDA-approved Embolic Protection Device (EPD).

          8. Non-contiguous lesions and long lesions (>3 cm).

          9. Qualitative characteristics of stenosis and stenosis-length of the carotid bifurcation
             (common carotid) and/or ipsilateral external carotid artery, that preclude safe sheath
             placement.

         10. Occlusive or critical ilio-femoral disease including severe tortuosity or stenosis
             that necessitates additional endovascular procedures to facilitate access to the
             aortic arch or that prevents safe and expeditious femoral access to the aortic arch.
             "String sign" of the ipsilateral common or internal carotid artery.

         11. Angiographic, CT, MR or ultrasound evidence of severe atherosclerosis of the aortic
             arch or origin of the innominate or common carotid arteries that would preclude safe
             passage of the sheath and other endovascular devices to the target artery as needed
             for carotid stenting.
```

</details>

**Who is right?** (mark one)
- [ ] Agent wrong: misread the note or the criterion
- [ ] Agent too strict: e.g. ignored a time window ("within 4 weeks") or a "unless" clause
- [ ] Label looks wrong (like the CPT-11 case)
- [ ] Unclear / needs more info

Notes:

---

## Patient 5 | NCT02750644

**Trial:** Postapproval Trial On Carotid Stenting in Patients With High Risk Vs Standard Risk for Open Carotid Endarterectomy(REAL)

**Agent reason:** The patient meets the asymptomatic inclusion criterion and has no documented exclusion factors.

<details><summary>Patient note</summary>

74M hx of CAD s/p CABG, EF 60% prior CVA (no residual deficits), HTN, HL, DMII, Moderate to Severe PVD was referred to cardiology for evaluation of PVD, and on examination patient was found to have carotid bruits. Upon further review of symptoms the pt reports + Occasional dizziness, no prior syncope occasional HA, Denies CP/SOB. No sensory or motor defects. He recalls that he might have had a stroke 10-15 years ago without any residual deficit. Prior to CABG he only had diaphoresis.
Further review of systems is notable for absence of chest pain, dyspnea on exertion, paroxysmal nocturnal dyspnea, orthopnea, palpitations, syncope or presyncope. He underwent Carotid U/S that showed significant bilateral carotid stenosis, L>R. Angiography revealed an 80% stenosis of the R ICA and a 90% L ICA stenosis. Cerebral angiography further revealed patent right ACA and MCA and patent left ACA and left MCA.
Past Medical History:
CAD s/p CABG in [**2154**] ([**Hospital1 112**])
Prior CVA
Bilateral carotid artery disease
Anemia
PVD
Hypertension
Diabetes c/b retinopathy and peripheral neuropathy
Cataracts s/p surgery
Thyroid nodule
Colon polyps s/p resection
Intermittent Lower back pain
Proteinuria
s/p right elbow fracture as a child
Arthritis

</details>

<details><summary>Full eligibility criteria</summary>

```
Inclusion Criteria:

          -  Symptomatic patients who have a transient ischemic attack, amaurosis fugax, or minor
             nondisabling stroke in the distribution of the study artery within 180 days of
             inclusion and have been shown carotid artery stenosis ≥50% by angiography, ≥70% by
             ultrasound, or ≥70% by CT angiography or MR angiography if ultrasound is 50% to 69%

          -  Asymptomatic patients who have carotid artery stenosis of ≥60% by angiography, ≥70% by
             ultrasound, or ≥80% by CT angiography or MR angiography if ultrasound is 50% to 69%

        Exclusion Criteria:

          -  Patient is unable to respond to external questions and stimuli and to exert a pressure
             with the contralateral hand

          -  Patient has an myocardial infarction within 72 hours prior to carotid stenting

          -  Patient has a major residual neurological deficit (stroke scales: Barthel ≤ 60, NIH ≥
             15 or Rankin >3) at pre-procedure neurological exam

          -  Patient had a transient ischemic attack (TIA) or amaurosis fugax within 48 hours prior
             to index procedure

          -  Patient had a stroke or retinal artery occlusion within 1 month prior to index
             procedure

          -  Patient has severe chronic renal failure (creatinine > 2.5mg/dL)

          -  The target carotid artery is completely occluded

          -  The common carotid artery ostium has stenosis that required treatment

          -  The presence of ipsilateral intracranial stenosis that requires treatment

          -  The inability to position a stiff 0.035" guidewire in the external carotid artery

          -  Contralateral occlusion of internal carotid artery and vertebral arteries
```

</details>

**Who is right?** (mark one)
- [ ] Agent wrong: misread the note or the criterion
- [ ] Agent too strict: e.g. ignored a time window ("within 4 weeks") or a "unless" clause
- [ ] Label looks wrong (like the CPT-11 case)
- [ ] Unclear / needs more info

Notes:

---

## Patient 10 | NCT01920204

**Trial:** Midostaurin in Indolent Systemic Mastocytosis

**Agent reason:** All applicable inclusion and exclusion criteria are met or unknown, with no failures.

<details><summary>Patient note</summary>

Pt is a 22yo F otherwise healthy with a 5 yr history of the systemic mastocytosis, with flares normally 3/year, presenting with flushing and tachycardia concerning for another flare. This is patient's 3rd flare in 2 months, while still on steroid taper which is new for her. She responded well to 125 mg IV steroids q 8 hrs and IV diphenydramine in addition to her continuing home regimen. CBC was at her baseline, w/normal differential. Serum tryptase revealed a high value at 84. The patient failed aspirin challenge due to adverse reaction. She was stabilized on IV steroids and IV benadryl and transferred back to the medical floor. She continued on her home histamine receptor blockers and was transitioned from IV to PO steroids and benadryl and observed overnight and was discharged on her home meds, prednisone taper, GI prophylaxis with PPI, Calcium and vitamin D, and SS bactrim for PCP.

</details>

<details><summary>Full eligibility criteria</summary>

```
Inclusion Criteria:

          -  Patients with Indolent Systemic Mastocytosis (ISM) or Smouldering Systemic
             Mastocytosis (SSM) according to the WHO criteria

          -  Presence of the D816V c-KIT mutation

          -  Serum tryptase > 20 mg/l

          -  Serious mediator-related symptoms that cannot be controlled by H1 and H2 blocking
             drugs. Symptoms will be scored by an adapted MSAF (mastocytosis symptom assessment
             form) with at least:

               -  a pre-study score of 4 or more on 3 non-related items,

               -  or a pre-study score of 5 or more on 2 non-related items.

               -  one item from the scoring list can be replaced by flushes 7 or more per week or
                  anaphylactic attacks 1 or more per week.

          -  Age >18 years

          -  Willingness to apply optimal contraceptive measures (double barrier method, both men
             and women) for women below the age of 55, men at all ages; for both: if sexually
             active.

          -  Written informed consent

        Exclusion Criteria:

          -  Aggressive systemic mastocytosis, mast cell leukemia, or ASM with or without
             accompanying non-clonal related non-mast cell disorder (SM-ANHMD).

          -  Any known other present malignancy, non-melanoma skin cancers excluded

          -  History of malignancy within the last 5 years, non-melanoma skin cancers excluded

          -  Any serious comorbidity interfering with therapy compliance and follow-up compliance

          -  Pregnancy

          -  Patients not willing or who are not able to comply with contraceptive measures
```

</details>

**Who is right?** (mark one)
- [ ] Agent wrong: misread the note or the criterion
- [ ] Agent too strict: e.g. ignored a time window ("within 4 weeks") or a "unless" clause
- [ ] Label looks wrong (like the CPT-11 case)
- [ ] Unclear / needs more info

Notes:

---

## Patient 10 | NCT00831974

**Trial:** Efficacy of AB1010 in Patients With Systemic Indolent Mastocytosis

**Agent reason:** No exclusion criteria are violated and the available information does not definitively fail any inclusion criteria.

<details><summary>Patient note</summary>

Pt is a 22yo F otherwise healthy with a 5 yr history of the systemic mastocytosis, with flares normally 3/year, presenting with flushing and tachycardia concerning for another flare. This is patient's 3rd flare in 2 months, while still on steroid taper which is new for her. She responded well to 125 mg IV steroids q 8 hrs and IV diphenydramine in addition to her continuing home regimen. CBC was at her baseline, w/normal differential. Serum tryptase revealed a high value at 84. The patient failed aspirin challenge due to adverse reaction. She was stabilized on IV steroids and IV benadryl and transferred back to the medical floor. She continued on her home histamine receptor blockers and was transitioned from IV to PO steroids and benadryl and observed overnight and was discharged on her home meds, prednisone taper, GI prophylaxis with PPI, Calcium and vitamin D, and SS bactrim for PCP.

</details>

<details><summary>Full eligibility criteria</summary>

```
Inclusion Criteria:

          1. Patients with documented Indolent systemic mastocytosis with handicap (ISMwh) having
             at least 2 infiltrated* organs (skin and /or bone-marrow and/or internal organ).

          2. Bone-marrow, or skin or internal biopsy-documented mastocytosis and evaluable disease.

          3. The absence of an activating point mutation in the phosphotransferase domain of c-Kit
             such as D816V c-Kit mutation in at least one of the two infiltrated organs: bone
             marrow and/or skin and/or other tissue.

          4. Handicap defined as at least one of the following handicaps:

               -  a number of flush per day ≥ 1 ,

               -  a pruritus score ≥ 9 ,

               -  a number of stools per day ≥ 4 ,

               -  a Pollakyuria (on a per day basis) ≥ 8 ,

               -  a QLQ-C30 score ≥ 83 ,

               -  a Hamilton rating scale for depression ≥ 12

        Exclusion Criteria:

          1. Performance status > 2 (ECOG).

          2. Inadequate organ function, except if the abnormalities are due to involvement by mast
             cells
```

</details>

**Who is right?** (mark one)
- [ ] Agent wrong: misread the note or the criterion
- [ ] Agent too strict: e.g. ignored a time window ("within 4 weeks") or a "unless" clause
- [ ] Label looks wrong (like the CPT-11 case)
- [ ] Unclear / needs more info

Notes:

---

## Patient 10 | NCT02380222

**Trial:** Patient-Reported Outcome Questionnaire for Systemic Mastocytosis

**Agent reason:** The trial targets systemic mastocytosis and the patient meets all known inclusion criteria without any exclusion criteria.

<details><summary>Patient note</summary>

Pt is a 22yo F otherwise healthy with a 5 yr history of the systemic mastocytosis, with flares normally 3/year, presenting with flushing and tachycardia concerning for another flare. This is patient's 3rd flare in 2 months, while still on steroid taper which is new for her. She responded well to 125 mg IV steroids q 8 hrs and IV diphenydramine in addition to her continuing home regimen. CBC was at her baseline, w/normal differential. Serum tryptase revealed a high value at 84. The patient failed aspirin challenge due to adverse reaction. She was stabilized on IV steroids and IV benadryl and transferred back to the medical floor. She continued on her home histamine receptor blockers and was transitioned from IV to PO steroids and benadryl and observed overnight and was discharged on her home meds, prednisone taper, GI prophylaxis with PPI, Calcium and vitamin D, and SS bactrim for PCP.

</details>

<details><summary>Full eligibility criteria</summary>

```
Inclusion Criteria:

          -  Documented diagnosis of one of the following conditions based upon World Health
             Organization (WHO) diagnostic criteria: aggressive systemic mastocytosis (ASM),
             systemic mastocytosis with associated clonal hematologic non-mast cell lineage disease
             (SM-AHNMD), mast cell leukemia (MCL), smoldering systemic mastocytosis (SSM), indolent
             systemic mastocytosis (ISM)

          -  Diagnosis confirmed by bone marrow biopsy

          -  Fluency in English

          -  Willingness and ability to participate in a one-hour interview

        Exclusion Criteria:

          -  A condition or situation that would interfere with participation in an interview
             (e.g., cognitive impairment or disorder, alcohol or drug abuse)

          -  Known human immunodeficiency virus or acquired immunodeficiency syndrome-related
             illness

          -  Any other prior malignancy except for the following: Adequately treated basal cell or
             squamous cell skin cancer; In situ cervical cancer; Adequately treated Stage I or II
             cancer from which the subject is currently in complete remission, or other cancer from
             which the subject has been disease-free for 2 years
```

</details>

**Who is right?** (mark one)
- [ ] Agent wrong: misread the note or the criterion
- [ ] Agent too strict: e.g. ignored a time window ("within 4 weeks") or a "unless" clause
- [ ] Label looks wrong (like the CPT-11 case)
- [ ] Unclear / needs more info

Notes:

---

## Patient 10 | NCT03770273

**Trial:** Safety and Efficacy of Subcutaneous Sarilumab in Improving the Quality of Life in People With Indolent Systemic Mastocytosis

**Agent reason:** No exclusion criteria are met and the patient satisfies the age requirement; other criteria are unknown but not disqualifying.

<details><summary>Patient note</summary>

Pt is a 22yo F otherwise healthy with a 5 yr history of the systemic mastocytosis, with flares normally 3/year, presenting with flushing and tachycardia concerning for another flare. This is patient's 3rd flare in 2 months, while still on steroid taper which is new for her. She responded well to 125 mg IV steroids q 8 hrs and IV diphenydramine in addition to her continuing home regimen. CBC was at her baseline, w/normal differential. Serum tryptase revealed a high value at 84. The patient failed aspirin challenge due to adverse reaction. She was stabilized on IV steroids and IV benadryl and transferred back to the medical floor. She continued on her home histamine receptor blockers and was transitioned from IV to PO steroids and benadryl and observed overnight and was discharged on her home meds, prednisone taper, GI prophylaxis with PPI, Calcium and vitamin D, and SS bactrim for PCP.

</details>

<details><summary>Full eligibility criteria</summary>

```
-  INCLUSION CRITERIA:

        Participants must meet all of the following criteria to be enrolled in this study:

          1. Male or female participant greater than or equal to 18 and < 75 years of age at
             screening.

          2. Enrolled on NIAID protocol 02-I-0277.

          3. Documented pathologic diagnosis of ISM.

          4. MC-QoL score of at least 25% (which suggests participant is at least somewhat affected
             by all McQoL questions).

          5. Willing and able to undergo a bone marrow biopsy and aspirate.

          6. Absolute neutrophil count (ANC) greater than or equal to 2000/mL.

          7. Hemoglobin greater than or equal to 12.0 g/dL (males), greater than or equal to 11
             g/dL (females).

          8. Platelet count greater than or equal to 150,000/microliters.

          9. Alanine transaminase (ALT) and aspartate transaminase (AST) < 1.5 times the upper
             limit of normal (ULN).

         10. Willing to allow storage of blood and bone marrow for future use in medical research.

         11. Willing to allow genetic testing on biospecimens.

         12. Able to provide informed consent.

         13. Participants who can become pregnant must agree to use adequate contraception when
             engaging in sexual activities that can result in pregnancy. Adequate contraception
             must be used consistently, beginning at least 1 month before the beginning of dosing
             and lasting until 3 months after the final dose of study drug. Acceptable methods of
             contraception include the following:

               -  Hormonal contraception (non-oral only).

               -  Male or female condom with spermicide.

               -  Diaphragm or cervical cap with a spermicide.

               -  Intrauterine device.

        EXCLUSION CRITERIA:

        Individuals meeting any of the following criteria will be excluded from study
        participation:

          1. Any abnormality that would be scored as a Grade 4 toxicity on the Common Terminology
             Criteria for Adverse Events (CTCAE) version 5.0. Only clinically significant lab
             results will deem the subject ineligible

          2. Infected with HIV or has other known immunodeficiency.

          3. Has an active infection, including localized infection.

          4. Active diverticulitis.

          5. Active or chronic viral hepatitis.

          6. Active or latent tuberculosis.

          7. Use of any other anti-IL-6 or anti-IL-6R agent within 1 year prior to the date
             informed consent was obtained.

          8. Use of cytoreductive therapy for mastocytosis within 1 year prior to the date informed
             consent was obtained.

          9. Known lymphoma or advanced and metastatic solid tumors on active therapy (including
             chemotherapy) within 1 year prior to the date informed consent was obtained

         10. Use of chemotherapy within 1 year prior to the date informed consent was obtained.

         11. Receipt of any marketed (eg, omalizumab) or investigational biologic or monoclonal
             antibody reported to affect mast cell activation within 5 half-lives prior to date
             informed consent was obtained.

         12. Receipt of intravenous (IV) immunoglobulin within 30 days prior to the date informed
             consent was obtained.

         13. Receipt of live attenuated vaccines within 30 days prior to the date informed consent
             was obtained.

         14. History of alcohol or drug/abuse within 12 months prior to date informed consent was
             obtained.

         15. Is allergic to any component of the sarilumab formulation.

         16. Pregnant or breastfeeding.

         17. Any condition that, in the opinion of the investigator, contraindicates participation
             in this study.
```

</details>

**Who is right?** (mark one)
- [ ] Agent wrong: misread the note or the criterion
- [ ] Agent too strict: e.g. ignored a time window ("within 4 weeks") or a "unless" clause
- [ ] Label looks wrong (like the CPT-11 case)
- [ ] Unclear / needs more info

Notes:

---

# Tally

| | Agent wrong | Too strict | Label wrong | Unclear |
|---|---|---|---|---|
| Eligible -> excluded | | | | |
| Excluded -> eligible | | | | |
