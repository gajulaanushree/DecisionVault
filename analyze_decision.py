from hindsight_client import Hindsight

HINDSIGHT_API_KEY = "hsk_ff3611c93b00dab2c7cf1e225877df44_a1d9e37c16b5c62a"

client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=HINDSIGHT_API_KEY
)

BANK_ID = "decisionvault"

new_decision = """
Should NovaTech launch an AI-powered social sharing feature?

Reason:
Our competitor recently launched a similar feature and we are worried
about falling behind.

Expected outcome:
Increase user engagement by 15%.
"""

print("\n========================================")
print("        DECISIONVAULT ANALYSIS")
print("========================================\n")

print("NEW DECISION:")
print(new_decision)

print("\nSearching company memory...\n")

# Find relevant historical decisions
result = client.recall(
    bank_id=BANK_ID,
    query="""
    What previous company decisions were influenced by competitors,
    copying competitor features, or fear of falling behind competitors?
    What happened afterward and what lessons were learned?
    """,
    
)

print("========================================")
print("        RELEVANT MEMORIES")
print("========================================\n")

for i, memory in enumerate(result.results, start=1):
    print(f"MEMORY {i}")
    print(memory.text)
    print("\n----------------------------------------\n")

print("\n========================================")
print("        AI DECISION INSIGHT")
print("========================================\n")

# Ask Hindsight to reason over company memory
response = client.reflect(
    bank_id=BANK_ID,
    query="""
    A product team is considering launching an AI-powered social sharing
    feature mainly because a competitor launched a similar feature.

    Based only on the company's stored decision history:

    1. Have we made similar competitor-driven decisions before?
    2. What happened?
    3. What lesson should we apply to this new decision?
    4. Give a short practical recommendation.

    Be specific and mention the relevant past decisions.
    """
)

print(response.text)

print("==========================================")
print("MEMORY EVIDENCE")
print("==========================================")

if response.based_on:
    for source in response.based_on:
        print(source)
else:
    print("Hindsight did not return separate source evidence for this reflection.")
client.close()