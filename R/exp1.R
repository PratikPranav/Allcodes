h<-"hello"
h

w="world"
print(w)

s1<-10
s2=20
s1+s2

# Create a numeric vector using c()
numeric_vector <- c(1, 2, 3, 4, 5)
print(numeric_vector)

vector <- c(1, 2, 3, 4, 5)
length(vector)

numbers <- c(1, 2, 3, 4, 5)
# Use the sum() function to calculate the sum of the vector elements
total_sum <- sum(numbers)


# Create a sample data frame
data <- data.frame(
  Name = c("Alice", "Bob", "Charlie", "David", "Eve", "Frank"),
  Age = c(25, 30, 22, 28, 35, 27)
)

# Use head() to view the first few rows of the data frame
head(data)
tail(data)



# Create a numeric vector
numeric_vector <- c(12, 15, 17, 20, 22, 25)

# Use summary() to summarize the numeric data
summary(numeric_vector)

#The output will display statistics like minimum, 1st quartile, median, mean, 3rd quartile, and maximum.



# Create a scatter plot using plot() with two numeric vectors
x <- c(1, 2, 3, 4, 5)
y <- c(2, 4, 1, 5, 3)
plot(x, y, main = "Scatter Plot", xlab = "X-axis", ylab = "Y-axis")



# Get help for the `mean` function
help("mean")
# Shorthand to get help for the `mean` function
?mean


# To give an examples for the specified command, here it is eg of readline
example("readline")


# Create a sequence of integers from 1 to 10 with a step size of 2
sequence <- seq(from = 1, to = 10, by = 2)
print(sequence)


# Replicate the values 1, 2, and 3 each five times
repeated_values <- rep(c(1, 2, 3), times = 5)
print(repeated_values)


# Create a matrix
mat <- matrix(1:12, nrow = 3, ncol = 4)

# Get the dimensions of the matrix
matrix_dimensions <- dim(mat)
print(matrix_dimensions)



# List objects in the current environment
objects_in_environment <- ls()
print(objects_in_environment)



# Create an object
my_variable <- 42

# Remove the object
rm(my_variable)

# Verify that the object is removed
print(ls())



# Create a factor variable
colors <- factor(c("Red", "Blue", "Red", "Green", "Blue", "Red", "Green", "Blue", "Red"))

# Create a frequency table
color_counts <- table(colors)
print(color_counts)


