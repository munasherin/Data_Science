library(class)

set.seed(1)  # makes tie-breaking repeatable

survey <- read.csv("survey.csv", stringsAsFactors = TRUE)

student <- data.frame(X = 5, Y = 7)

survey1 <- survey[, c("X", "Y")]   # select by name, not position

pred <- knn(train = survey1, test = student, cl = survey$Z, k = 3)

cat("Predicted Classification of Student:\n")
print(pred)