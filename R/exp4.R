# Install and load the necessary package (if not installed)
if (!require(class)) {
  install.packages("class")
  library(class)
}

# Load the Iris dataset (it's a built-in dataset in R)
data(iris)

# Split the data into training and testing sets
set.seed(123)
sample_indices <- sample(1:nrow(iris), 0.7 * nrow(iris))  # 70% for training
train_data <- iris[sample_indices, ]
test_data <- iris[-sample_indices, ]

# Define the predictor variables (features) and the target variable
predictors <- c("Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width")
target <- "Species"

# Train the KNN model
knn_model <- knn(train = train_data[, predictors], 
                 test = test_data[, predictors], 
                 cl = train_data[, target], 
                 k = 3)

# Print the confusion matrix to evaluate the model
conf_matrix <- table(knn_model, test_data[, target])
print("Confusion Matrix:")
print(conf_matrix)

# Calculate accuracy
accuracy <- sum(diag(conf_matrix)) / sum(conf_matrix)
cat("Accuracy:", accuracy, "\n")
