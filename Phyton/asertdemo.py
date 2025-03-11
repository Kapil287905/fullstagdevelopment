# assert:-it is an keyword and statement used to perform debugging of code
# It is useful to ensure that given condition is True. If condition is False
# then it will raise exception as "AssertException"

#syntax : assert condition, errormassage

# Votinf Eligibility

age = int(input("Enter age = "))
assert age >= 18, "Your age must be above 18 then only you are eligible to vote"