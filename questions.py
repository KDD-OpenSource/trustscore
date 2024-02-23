"""
"""




questions=[
"""Decisions made by the model are biased against certain groups or individuals
User inputs are requested in a biased manner
Performance differs for certain groups or can only be applied to certain groups
The dataset is not representative of the application (sampling bias)
The dataset includes protected attributes
The dataset perpetuates biases (e.g., is generated from unfiltered web data)""",
"""Risk of adversarial or inversion attacks not mitigated
The model does not generalize to different datasets
Repeated model executions do not generate the same or similar outputs
The dataset does not contain edge cases or outliers
The data is susceptible to distribution shifts
The data contains harmful anomalies or perturbations""",
"""It cannot be guaranteed, that the model was not tampered with
No output uncertainties are given
Changes made to the model cannot be tracked
It cannot be guaranteed, that the data was not tampered with
Changes made to the data cannot be tracked
Pronounced labeling uncertainties cannot be ruled out""",
"""The model’s decision-making process is not transparent
The model’s architecture is unknown or prohibits its interpretation
Stakeholders cannot validate the model’s outputs
No documentation of the data collection and annotation process
The dataset is not human understandable
Lack of clarity on how missing values or outliers are handled in the dataset""",
"""Decisions or internal representations could reveal sensitive information
Insufficient access control to proprietary model
Erroneous decisions might lead to critical consequences
Insufficient access control to proprietary data
Exposure of sensitive information through metadata or auxiliary data
Lack of transparent data governance policies (e.g., data usage agreements)"""]

questions=[q.split('\n') for q in questions]

subtasks=["Fairness", "Robustness","Integrity","Explainability","Safety"]



