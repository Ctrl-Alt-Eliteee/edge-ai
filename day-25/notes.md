Suppose you want to tune:

max_depth = [3,5]

and

min_samples_split = [2,5,10]
Questions

1. How many total combinations will Grid Search test?

6 combinations will be there

2. Why is Grid Search usually better than manually trying random values?

See, by guessing which value is better for accuracy. So it, the guess is very random. My guess, the chances that my guess is correct are very low. But if we do grid search test, that means it combines, it does a combination of all the values and it takes, it shows that which model is the best. That means which combination makes the best model

3. If your manager says:

"Let's test only one combination. That's enough."

Would you agree?

Why or why not?

And if my manager says let's test only one combination, that's enough. No, I won't agree with him because I have to try each and every combination. What if maximum depth three and minimum sample split 10 or 5 will work more nicer than maximum depth 5 and minimum sample split 2? This is just my assumption, okay. This is what I'm just saying that I won't agree with him because I'll tell him that we'll do grid search test, it will combine all the possible values, it will take all the possible combinations, and then It finds the best combination according to the evaluation metric we choose (for example, accuracy)