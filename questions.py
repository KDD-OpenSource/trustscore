"""
"""




questions=[
"""Decisions made by the model are biased against certain groups of people
Decisions made by the model are biased against some individuals
Inputs are requested in a biased manner
The model performs better or worse for certain groups of people
The model can only be used by/applied to a select group of people
The dataset is not representative of the application (sampling bias)
The dataset perpetuates historical or other biases
The authenticity of the dataset cannot be guaranteed
The dataset includes protected attributes
The dataset is generated from unfiltered web data""",
"""Risk of adversarial attacks
Risk of model inversion attacks
The model does not generalize to different datasets
The model behavior depends on external variables (e.g., internet, time)
Repeated model executions do not generate the same output
Adversaries could inject malicious data
The dataset is very noisy
The data is susceptible to distribution shifts
The data might look different during application (environmental changes)
The data might contain harmful anomalies""",
"""The model behavior is not monitored
The model is not verifiable with access to the model
The model is only verifiable with access to the model
No output uncertainties are given
The model is not open source
The collected data is not verified
The collected data is not publicly available
The data collection method is unknown
A data subset was created based on human biases
Uncertainties in the data are unavailable""",
"""The model’s decisions are not explainable
The model’s architecture is not known
Stakeholders/experts cannot validate the model’s outputs
The type of model makes it difficult to interpret
Illusion of Explanatory Depth
Lack of documentation regarding the data collection process
Incomplete information about the source and context of the dataset
The dataset is not human understable
Lack of clarity on how missing values or outliers are handled in the dataset
Lack of information about the demographics targeted during data collection""",
"""Decisions could inadvertently reveal sensitive information
Parameters or internal representations reveal sensitive information
Insufficient access control, leading to unauthorized access to the model
Proprietary architecture is not sufficiently protected from unauthorized access
Erroneous model decisions might lead to critical consequences
The proprietary dataset is not sufficiently protected from unauthorized access
The dataset is publicly available, while containing private information
Lack of secure transmission mechanisms when sharing or storing sensitive data
Exposure of sensitive information through metadata or auxiliary data
Lack of transparent data governance policies (e.g., data usage agreements)"""]

questions=[q.split('\n') for q in questions]

subtasks=["Fairness", "Robustness","Integrity","Explainability","Safety"]



