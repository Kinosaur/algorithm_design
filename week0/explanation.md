# Apple Buying Problem - Simple Explanation

## What's the Problem?

You go to a store to buy **exactly 5kg** of apples.

But the store is weird:
- Apples come in **pre-packed bags** (1kg bag, 2kg bag, 3kg bag, etc.)
- Each bag has its own **price**
- Some bags might be **sold out** (shown as -1)
- You can only buy **maximum N bags** (N = number of friends)

**Question:** What's the **cheapest** way to get exactly 5kg? If impossible, return -1.

---

## Real-Life Example

**You need: 5kg**  
**Max bags: 5**

**Available bags:**
- 1kg = 1 rupee
- 2kg = 2 rupees  
- 3kg = 4 rupees
- 4kg = 5 rupees
- 5kg = sold out (-1)

**Ways to make 5kg:**
1. Buy **five 1kg bags** → 1+1+1+1+1 = **5 rupees** ✓ CHEAPEST!
2. Buy **1kg + 4kg** → 1+5 = 6 rupees
3. Buy **2kg + 3kg** → 2+4 = 6 rupees

**Answer: 5 rupees**

---

## How Does the Code Work?

Think of it like filling a piggy bank:

### The DP Array
```
dp[0] = 0    "0kg costs 0 rupees"
dp[1] = ?    "What's cheapest way to get 1kg?"
dp[2] = ?    "What's cheapest way to get 2kg?"
dp[3] = ?    "What's cheapest way to get 3kg?"
...
dp[5] = ?    "What's cheapest way to get 5kg?" ← This is what we want!
```

### The Strategy

**Round 1: Use only 1 bag**
- Can I make 1kg? Yes! Buy 1kg bag → `dp[1] = 1`
- Can I make 2kg? Yes! Buy 2kg bag → `dp[2] = 2`
- Can I make 3kg? Yes! Buy 3kg bag → `dp[3] = 4`
- Can I make 4kg? Yes! Buy 4kg bag → `dp[4] = 5`
- Can I make 5kg? No! 5kg bag is sold out → `dp[5] = -1`

**Round 2: Use up to 2 bags**
- For 5kg: Can I use 1kg + 4kg? Yes! → 1+5 = 6 rupees
- For 5kg: Can I use 2kg + 3kg? Yes! → 2+4 = 6 rupees
- Best so far: `dp[5] = 6`

**Round 3: Use up to 3 bags**
- For 5kg: Can I use 1kg + 1kg + 3kg? Yes! → 1+1+4 = 6 rupees
- For 5kg: Can I use 1kg + 2kg + 2kg? Yes! → 1+2+2 = 5 rupees ✓ BETTER!
- Best so far: `dp[5] = 5`

**Round 4 & 5:** No better combinations found

**Final Answer: dp[5] = 5 rupees**

---

## The Key Idea

Instead of trying ALL possible combinations (which would take forever), we:

1. **Start small**: Figure out cheapest way for 1kg, 2kg, 3kg...
2. **Build up**: Use what we already know to solve bigger weights
3. **Remember**: Save the best solution for each weight so we don't recalculate

This is called **Dynamic Programming** - solving big problems by remembering solutions to smaller problems!

---

## Simple Analogy

It's like climbing stairs:
- You can climb 1 step, 2 steps, or 3 steps at a time
- Each step type costs different energy
- You want to reach step 5 with minimum energy
- You figure out best way to reach step 1, then step 2, then step 3...
- When you reach step 5, you already know the best way!

That's exactly what our code does! 🎯
