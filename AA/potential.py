def cost_calc(size):
    insertionCost=1
    doublingCost=0
    totalCost=insertionCost+doublingCost
    prevSize=1
    currSize=1
    potential=1
    prevPotential=0
    amortizedCost=totalCost+potential
    print("i\tprevious_size\tcurrent_size\tdoubling_cost\tinsertion_cost\ttotal_cost\tpotential\tamortized_cost")  
    for i in range(1,size+1):
        print(f"\n{i}\t{prevSize}\t{currSize}\t{doublingCost}\t{insertionCost}\t{totalCost}\t{potential}\t{amortizedCost}")
        prevSize=currSize
        if i==currSize:
            currSize*=2
            doublingCost=currSize-prevSize
        else:
            doublingCost=0
        totalCost=insertionCost+doublingCost 
        prevPotential=potential
        potential=2*i-currSize
        amortizedCost=totalCost+potential-prevPotential
cost_calc(16)