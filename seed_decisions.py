from hindsight_client import Hindsight

HINDSIGHT_API_KEY = "hsk_ff3611c93b00dab2c7cf1e225877df44_a1d9e37c16b5c62a"

client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=HINDSIGHT_API_KEY
)

BANK_ID = "decisionvault"

decisions = [

    """
    Company: NovaTech
    Decision: Launch dark mode.
    Reason: 40% of users requested dark mode.
    Expected outcome: 15% increase in engagement.
    Actual outcome: 2% increase in engagement.
    Result: Underperformed.
    Lesson: User requests alone did not guarantee a large engagement increase.
    """,

    """
    Company: NovaTech
    Decision: Copy a competitor's social sharing feature.
    Reason: A major competitor launched it.
    Expected outcome: 10% increase in user activity.
    Actual outcome: 1% increase.
    Result: Failed.
    Lesson: Competitor launches alone are weak evidence of customer demand.
    """,

    """
    Company: NovaTech
    Decision: Simplify the onboarding process.
    Reason: Analytics showed many users leaving during signup.
    Expected outcome: 8% increase in activation.
    Actual outcome: 13% increase.
    Result: Successful.
    Lesson: Decisions based on actual user behavior produced strong results.
    """,

    """
    Company: NovaTech
    Decision: Launch a premium subscription.
    Reason: Many active users requested advanced features.
    Expected outcome: 5% conversion.
    Actual outcome: 7% conversion.
    Result: Successful.
    Lesson: Premium features worked when they addressed a clear user need.
    """,

    """
    Company: NovaTech
    Decision: Increase product price by 20%.
    Reason: Competitors had higher prices.
    Expected outcome: Revenue increase without major churn.
    Actual outcome: Churn increased significantly.
    Result: Failed.
    Lesson: Competitor pricing was not enough evidence to change our pricing.
    """,

    """
    Company: NovaTech
    Decision: Improve mobile page performance.
    Reason: Mobile users had slow loading times.
    Expected outcome: 5% increase in conversion.
    Actual outcome: 11% increase.
    Result: Successful.
    Lesson: Fixing measurable user problems created strong business impact.
    """,

    """
    Company: NovaTech
    Decision: Build an AI chatbot for the homepage.
    Reason: AI products were becoming popular.
    Expected outcome: More website engagement.
    Actual outcome: Very little change.
    Result: Underperformed.
    Lesson: Adding popular technology without a clear customer problem produced weak results.
    """,

    """
    Company: NovaTech
    Decision: Add automated email reminders.
    Reason: Many users started tasks but did not finish them.
    Expected outcome: 10% increase in task completion.
    Actual outcome: 16% increase.
    Result: Successful.
    Lesson: Reminders worked when connected to an existing user behavior problem.
    """,

    """
    Company: NovaTech
    Decision: Launch a feature because a competitor announced it.
    Reason: Concern about falling behind competitors.
    Expected outcome: Maintain market position.
    Actual outcome: Low adoption.
    Result: Failed.
    Lesson: Fear of competitors should not replace customer validation.
    """,

    """
    Company: NovaTech
    Decision: Remove three rarely used settings.
    Reason: Product analytics showed extremely low usage.
    Expected outcome: Simpler interface with no negative impact.
    Actual outcome: Support requests decreased.
    Result: Successful.
    Lesson: Product analytics can identify unnecessary complexity.
    """,

    """
    Company: NovaTech
    Decision: Launch a referral program.
    Reason: Existing customers frequently recommended the product.
    Expected outcome: 5% increase in new users.
    Actual outcome: 9% increase.
    Result: Successful.
    Lesson: Existing customer behavior can be a strong signal for new initiatives.
    """,

    """
    Company: NovaTech
    Decision: Build a social feed.
    Reason: Social feeds were popular in competing products.
    Expected outcome: Higher daily engagement.
    Actual outcome: Engineering cost was high and engagement barely changed.
    Result: Failed.
    Lesson: Popular competitor features should be validated before major development.
    """,

    """
    Company: NovaTech
    Decision: Improve checkout by reducing the number of steps.
    Reason: Analytics showed users abandoning checkout.
    Expected outcome: 5% increase in completed purchases.
    Actual outcome: 12% increase.
    Result: Successful.
    Lesson: Removing friction from a measured problem produced a strong result.
    """,

    """
    Company: NovaTech
    Decision: Launch a large advertising campaign.
    Reason: A competitor had increased advertising spending.
    Expected outcome: Large increase in new customers.
    Actual outcome: Traffic increased but conversions stayed low.
    Result: Underperformed.
    Lesson: More traffic does not solve a weak conversion experience.
    """,

    """
    Company: NovaTech
    Decision: Improve search based on customer complaints.
    Reason: Customers reported difficulty finding products.
    Expected outcome: 10% increase in successful searches.
    Actual outcome: 18% increase.
    Result: Successful.
    Lesson: Repeated customer problems can be strong evidence for product decisions.
    """
]

print("Starting DecisionVault memory setup...\n")

for i, decision in enumerate(decisions, start=1):
    try:
        client.retain(
            bank_id=BANK_ID,
            content=decision
        )
        print(f"Decision {i}/15 stored successfully.")
    except Exception as e:
        print(f"Decision {i} failed: {e}")

print("\n================================")
print("DecisionVault memory is ready!")
print("15 historical decisions added.")
print("================================")