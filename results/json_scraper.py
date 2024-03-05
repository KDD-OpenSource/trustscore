import os
import json
import matplotlib.pyplot as plt

# Get the current working directory
folder_path = os.getcwd()

# Initialize dictionaries to store weights, categories, and results per model and name
weights_per_model_name = {}
results_per_model_name = {}
scores_per_model_name = {}

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json') and filename.startswith('score_'):
        # Extract model name and name from filename
        model_name = filename.split('_')[1]
        name = filename.split('_')[2].split('.')[0]

        # Load JSON data from file
        with open(os.path.join(folder_path, filename), 'r') as file:
            data = json.load(file)

        # Extract weights, categories, and results from the JSON data
        weights = [info['weight'] for info in data['infos']]
        scores = [info['score'] for info in data['infos']]
        categories = [info['task'] for info in data['infos']]
        result = data['result']

        # Store weights and result in dictionaries
        key = (model_name, name)
        weights_per_model_name.setdefault(key, []).extend(weights)
        scores_per_model_name.setdefault(key, []).extend(scores)
        results_per_model_name[key] = result

# Print weights per model and category
#print("Weights per Model and Category:")
#for (model, name), weights in weights_per_model_name.items():
#    print(f"Model: {model}, Name: {name}")
#    categories = [info['task'] for info in data['infos']]
#    for category, weight in zip(categories, weights):
#        print(f"  Category: {category}, Weight: {weight}")
#    print()
scores_per_model_name = {k: scores_per_model_name[k] for k in sorted(scores_per_model_name.keys())}
results_per_model_name = {k: results_per_model_name[k] for k in sorted(results_per_model_name.keys())}

print("Scores per Model and Category:")
for (model, name), scores in scores_per_model_name.items():
    print(f"Model: {model}, Name: {name}")
    categories = [info['task'] for info in data['infos']]
    for category, score in zip(categories, scores):
        print(f"  Category: {category}, Score: {score}")
    print()

# Print results per model and name
print("Results per Model and Name:")
for (model, name), result in results_per_model_name.items():
    print(f"Model: {model}, Name: {name}, Result: {result}")

# Initialize dictionary to store results for each model
model_results = {model: [] for model, _ in weights_per_model_name.keys()}

# Append results to corresponding model in the dictionary
for (model, _), result in results_per_model_name.items():
    model_results[model].append(result)

# Calculate average, min, and max results for each model
for model, results in model_results.items():
    avg_result = sum(results) / len(results)
    min_result = min(results)
    max_result = max(results)
    print(f"{model.capitalize()}: Avg: {avg_result}, Min: {min_result}, Max: {max_result}")

# Initialize lists to store data for plotting
models = []
avg_results = []
min_results = []
max_results = []

# Iterate over the model results
for model, results in model_results.items():
    # Calculate average, minimum, and maximum results
    avg_result = sum(results) / len(results)
    min_result = min(results)
    max_result = max(results)
    
    # Append data to lists
    models.append(model.capitalize())
    avg_results.append(avg_result)
    min_results.append(min_result)
    max_results.append(max_result)

# Plotting
plt.figure(figsize=(12, 6))

# Line plot
plt.subplot(1, 2, 1)
plt.plot(models, avg_results, label='Average Result', marker='o')
plt.plot(models, min_results, label='Minimum Result', marker='s')
plt.plot(models, max_results, label='Maximum Result', marker='^')
plt.title('Results per Model')
plt.xlabel('Model')
plt.ylabel('Result')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# Scatter plot
plt.subplot(1, 2, 2)
for model, results in model_results.items():
    plt.scatter([model] * len(results), results, label=model.capitalize())
plt.title('Scatter Plot of Results per Model')
plt.xlabel('Model')
plt.ylabel('Result')
#plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
