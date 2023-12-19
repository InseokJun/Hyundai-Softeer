"""
Question - Determine the size of a new vehicle to achieve target sales
"""

# Receive Input Data (Consumer-Related Information)
consumer_num = int(input())                                                 # Numbers of Consumers
consumer_proposal = []                                                      # Information suggested by consumers

for i in range(consumer_num):                                               # Repeat as many times as there are consumers
    
    temp = list(map(int, input().split()))                                  # Receive consumer suggestion information according to the input format
    
    for j in range(temp[0]):                                                # First argument of proposal information indicates the number of proposals by one person
        
        consumer_proposal.append([temp[2 * j+1], temp[2 * j+2], i + 1])     # New car's size, Price paid, and Consumer ID are stored in one list
    
# Receive Input Data (Scenario-Related Information)
scenario_num = int(input())                                                 # Number of Scenarios
temp = list(map(int, input().split()))                                      # Receive sales information within the scenario
scenario = []                                                               # List to store modified final scenario information

for i in range(scenario_num):                                               # Repeat as many times as there are scenarios
    scenario.append([temp[i], i + 1])                                       # Target sales, target sales ID to indicate order are stored in one list


# Solve the Question
consumer_proposal.sort()                                                     # Sort the list based on the size of the new car
scenario.sort()                                                              # Sort the list based on the target sales 

amount_per_consumer = [0] * (consumer_num+1)                                 # Suggested amount per person
revenue = 0                                                                  # Benefits from selling 
sidx = 0                                                                     # Index to access the scenario list

for i in range(len(consumer_proposal)):                                      # Repeat as many times as there are proposals
    
    size = consumer_proposal[i][0]                                           # New car size
    payment = consumer_proposal[i][1]                                        # Amount the consumer said he would pay
    consumer_ID = consumer_proposal[i][2]                                    # ID of the consumer who made the offer
    
    if payment > amount_per_consumer[consumer_ID]:                           # Compare the new offer amount to the existing amount for that consumer
        revenue += -amount_per_consumer[consumer_ID]+payment                 # Update revenue 
        amount_per_consumer[consumer_ID] = payment                           # Update amount per consumer

    while (sidx < scenario_num and scenario[sidx][0] <= revenue):            # When sales exceed target sales
        scenario[sidx].append(size)                                          # Add the minimum new car size that will achieve target sales as the last element in the list
        sidx += 1                                                            # Increase 1 to sidx
        
while (sidx < scenario_num):                                                 # When target sales cannot be achieved under any circumstances
    scenario[sidx].append(-1)                                                # Add -1 to match the problem conditions
    sidx += 1                                                                # Increase 1 to sidx
    
scenario.sort(key = lambda x:x[1])                                           # Resort by target sales ID in initial order to preserve output format


# Final Output
for i in scenario:
    print(i[2], end = " ")