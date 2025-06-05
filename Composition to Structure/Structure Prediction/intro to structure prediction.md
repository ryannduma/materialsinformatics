# From Composition to Structure: The SMACT Approach

You've mastered the art of finding chemically viable compositions through combinatorial screening and intelligent filtering. But here's the next challenge: **How do you predict what crystal structure those compositions will adopt?**

This is where **structure prediction** becomes crucial. Having a composition like "LiCoO₂" tells you the recipe - but will it form a layered structure (good for batteries) or a spinel structure (different properties)? The crystal structure determines the material's properties.

## The Challenge of Structure Prediction

Traditional structure prediction is extremely difficult:
- **Quantum mechanical calculations** are accurate but computationally expensive
- **Crystal structure databases** only contain known materials
- **Experimental synthesis** is time-consuming and may not work
- **Pure guessing** has astronomically low success rates

We need smarter approaches that leverage existing knowledge to predict new structures.

## SMACT's Substitution-Based Approach

SMACT's structure prediction module takes a data-driven approach based on a simple but powerful idea:

> **"Similar ions can often substitute for each other in crystal structures"**

If we know that Na⁺ and K⁺ behave similarly (both large, singly-charged cations), then we can predict that compounds like KCl might adopt the same structure as NaCl.

This approach is based on the methodology from Hautier et al., who showed that ionic substitution patterns can be learned from databases and used to predict new materials:

> Hautier, G., Fischer, C., Ehrlacher, V., Jain, A., and Ceder, G. (2011)  
> Data Mined Ionic Substitutions for the Discovery of New Compounds.  
> Inorganic Chemistry, 50(2), 656-663.  
> [doi:10.1021/ic102031h](https://pubs.acs.org/doi/10.1021/ic102031h)

## How It Works: The Substitution Strategy

The SMACT approach works in several steps:

### 1. **Build a Structure Database**
- Import known crystal structures from Materials Project/ICSD
- Create a searchable database of structure-composition relationships
- Focus on the most reliable, experimentally-validated structures

### 2. **Learn Substitution Patterns**
- Analyze which ionic substitutions occur frequently in nature
- Build probability models based on ionic size, charge, and electronegativity
- Create "lambda tables" that encode substitution likelihoods

### 3. **Predict New Structures**
- Take your target composition (e.g., from previous screening steps)
- Find similar compositions in the database
- Apply substitution rules to predict likely crystal structures
- Rank predictions by probability

### 4. **Validate and Refine**
- Check chemical reasonableness of predictions
- Calculate formation energies if needed
- Provide confidence estimates based on similarity to known materials

## What Makes This Powerful

This approach offers several advantages:

- **Speed**: Much faster than ab initio crystal structure prediction
- **Chemical intuition**: Based on real substitution patterns from nature
- **Integration**: Works seamlessly with composition screening results
- **Interpretability**: You can understand why a structure was predicted
- **Scalability**: Can screen thousands of compositions quickly

## Building Toward CHEMELEON

The SMACT structure prediction approach represents the "classical" way of doing computational materials discovery:
- Start with known structures
- Apply chemical rules and statistical analysis
- Make incremental improvements through substitution

But what if we could go beyond incremental changes? What if we could generate entirely new crystal structures from scratch? This is where **CHEMELEON** comes in - representing the next generation of AI-driven structure generation.

## What You'll Learn

In this section, we'll explore:

### Practical Skills
- How to set up and use SMACT's structure prediction module
- Building and querying structure databases
- Implementing ionic substitution models
- Generating and ranking structure predictions

### Conceptual Understanding
- The principles behind substitution-based prediction
- How to interpret and validate predictions
- When this approach works well (and when it doesn't)
- How traditional methods prepare us for AI approaches

### Real Applications
- Predicting structures for battery materials
- Finding new phases in known chemical systems
- Screening large numbers of compositions for structure types
- Preparing inputs for more detailed computational studies

## Integration with Previous Learning

This section builds directly on everything you've learned:
- **Combinatorial Explosion**: Showed us the scale of chemical space
- **Chemical Filters**: Taught us to eliminate impossible combinations
- **Compositional/Stoichiometry Screening**: Generated viable compositions
- **Structure Prediction**: Now predicts crystal structures for those compositions

## The Path Forward

By the end of this section, you'll have solid grounding in traditional structure prediction methods. This foundation is essential for understanding and appreciating the revolutionary approaches that CHEMELEON brings to the field.

Ready to predict your first crystal structure? Let's dive into the world of ionic substitutions and data-driven prediction!