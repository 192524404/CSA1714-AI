import math

# Sample Dataset: [Outlook (0:Sunny, 1:Overcast, 2:Rain), Temp (0:Cool, 1:Mild, 2:Hot)] -> Play (0:No, 1:Yes)
data = [
    [0, 2, 0],
    [0, 2, 0],
    [1, 2, 1],
    [2, 1, 1],
    [2, 0, 1],
    [2, 0, 0],
    [1, 0, 1],
    [0, 1, 0],
    [0, 0, 1],
    [2, 1, 1],
]

def calculate_entropy(target_col):
    elements, counts = {}, {}
    for row in target_col:
        counts[row] = counts.get(row, 0) + 1
    entropy = 0.0
    for count in counts.values():
        prob = count / len(target_col)
        entropy -= prob * math.log2(prob)
    return entropy

def build_tree(data, features):
    labels = [row[-1] for row in data]
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    if not features:
        return max(set(labels), key=labels.count)

    base_entropy = calculate_entropy(labels)
    best_info_gain = -1
    best_feature = None

    for f_idx in features:
        feature_values = set(row[f_idx] for row in data)
        new_entropy = 0.0
        for val in feature_values:
            subset = [row for row in data if row[f_idx] == val]
            prob = len(subset) / len(data)
            new_entropy += prob * calculate_entropy([row[-1] for row in subset])
        
        info_gain = base_entropy - new_entropy
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = f_idx

    tree = {best_feature: {}}
    remaining_features = [f for f in features if f != best_feature]
    feature_values = set(row[best_feature] for row in data)

    for val in feature_values:
        subset = [row for row in data if row[best_feature] == val]
        tree[best_feature][val] = build_tree(subset, remaining_features)

    return tree

# Build Decision Tree
features_indices = [0, 1]
tree = build_tree(data, features_indices)

print("Decision Tree Structure built successfully:")
print(tree)
