# Load the required libraries
library(factoextra)

# Load the iris dataset
data(iris)

# Select the relevant columns for clustering (e.g., sepal length and width)
# You can choose different columns depending on your needs
selected_features <- iris[, c("Sepal.Length", "Sepal.Width")]

# Perform K-means clustering with K=3
k <- 3
kmeans_result <- kmeans(selected_features, centers = k)

# Create a data frame for cluster centers
centers_df <- data.frame(
  Sepal.Length = kmeans_result$centers[, 1],
  Sepal.Width = kmeans_result$centers[, 2]
)

# Create a cluster visualization with enclosed boundaries
cluster_visualization <- fviz_cluster(kmeans_result, data = selected_features)

# Print the cluster visualization
print(cluster_visualization)
