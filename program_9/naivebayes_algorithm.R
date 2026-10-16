library(e1071)

symptoms <- read.csv("symptoms.csv", stringsAsFactors = TRUE)

symptoms_train <- symptoms[, c("Chills", "RunningNose", "Headache", "Fever")]

# Test data uses the same levels as the training data
symptoms_test <- data.frame(
  Chills      = factor("Y",    levels = levels(symptoms$Chills)),
  RunningNose = factor("N",    levels = levels(symptoms$RunningNose)),
  Headache    = factor("mild", levels = levels(symptoms$Headache)),
  Fever       = factor("Y",    levels = levels(symptoms$Fever))
)

classifier_cl <- naiveBayes(symptoms_train, symptoms$HasFlu)

print(classifier_cl)

symptoms_test_pred <- predict(classifier_cl, symptoms_test)

cat("Prediction of Flu:\n")
print(symptoms_test_pred)