
# Load the rpart package
library(rpart)

# Load the iris dataset
data(iris)

# Define the formula
formula <- Species ~ Sepal.Length + Sepal.Width + Petal.Length + Petal.Width

# Create a decision tree model
tree_model <- rpart(formula, data = iris)

# Load the rpart.plot package
library(rpart.plot)

# Plot the decision tree
prp(tree_model, type = 4, extra = 1, under = TRUE, varlen = 0, cex = 0.8)



