# Materials Informatics Advanced Practical: Course Overview

Welcome to this comprehensive course on computational materials discovery! In this practical course, you'll learn how to use ml/ai and informatics tools to learn about the materials design process behind batteries, solar cells, catalysts, semiconductors and a variety of other materials applications.

At the heart of this journey is **SMACT** (Semiconducting Materials from Analogy and Chemical Theory), a powerful Python toolkit that enables rapid screening of millions of potential materials using chemical rules and data-driven approaches. You'll also explore cutting-edge AI methods like **CHEMELEON**, which can generate crystal structures from simple text descriptions. With brief advanced walkthroughs into the world of forcefields, and DFT.

## Course Overview

This course is structured to provide both theoretical knowledge and practical skills in materials informatics. Below is an overview of the key topics we will cover:

---

## 1. Combinatorial Explosion and Chemical Space Generation

**Description:**

- Understand the concept of combinatorial explosion in materials science and its implications for materials discovery.
- Utilize SMACT's capabilities to generate extensive lists of elemental compositions.
- Prepare these compositions as inputs for machine learning models and other screening workflows.

**Learning Outcomes:**

- Grasp the challenges posed by vast chemical spaces.
- Efficiently generate and manage large datasets of potential material compositions.

---

## 2. Application of Chemical Filters

**Description:**

- Learn about chemical filters—a set of rules applied to reduce chemical spaces to viable candidates.
- Use a modified `smact_filter` function to apply these rules to generated compositions.
- Convert filtered results into dataframes with features suitable for machine learning algorithms.

**Learning Outcomes:**

- Apply chemical filters to streamline candidate selection.
- Prepare datasets for machine learning applications.

---

## 3. Compositional Screening and Phase Diagram Analysis

**Description:**

- Use SMACT to screen chemical spaces for specific element combinations (e.g., {Cu, Ti, O}).
- Generate phase diagrams illustrating all allowable and forbidden composition possibilities.
- Interpret these diagrams to identify promising material candidates.

**Learning Outcomes:**

- Perform targeted compositional screenings.
- Analyze and interpret phase diagrams for material selection.

---

## 4. Stoichiometry Screening

**Description:**

- Explore methods to find compounds that satisfy specific stoichiometries (e.g., perovskite **ABX₃**).
- Utilize a modified SMACT filter function to identify such compounds.
- Assess the potential of these compounds for further study.

**Learning Outcomes:**

- Conduct stoichiometry-based screenings.
- Identify and evaluate compounds matching desired stoichiometric formulas.

---

## 5. Composition to Structure Techniques

### 5.1 Structure Prediction with SMACT

**Description:**

- Learn about SMACT's structure prediction submodule based on ionic substitution, inspired by Hautier et al.'s 2011 paper.
- Set up a database of SMACT-compatible structures.
- Assign compositions to known crystal structures using the structure prediction tool.

**Learning Outcomes:**

- Utilize ionic substitution methods for structure prediction.
- Build and manage structural databases for materials exploration.

### 5.2 Crystal Structure Generation with CHEMELEON

**Description:**

- Explore **CHEMELEON**, a state-of-the-art generative AI model that creates crystal structures from text descriptions.
- Learn how CHEMELEON differs from traditional substitution-based methods by generating structures from scratch.
- Practice both Crystal Structure Prediction (CSP) for specific formulas and De Novo Generation (DNG) for exploring unknown chemical space.
- Compare the complementary strengths of SMACT's physics-based approach with CHEMELEON's AI-driven generation.

**Learning Outcomes:**

- Generate crystal structures using natural language prompts and chemical formulas.
- Understand the paradigm shift from substitution to generation in materials discovery.
- Evaluate when to use traditional vs. AI-driven structure prediction methods.

---

## 6. Advanced Methods

**Description:**

- Dive into advanced topics through interactive notebooks.
- Understand the thermodynamics of materials and their role in materials discovery.
- Explore Machine Learning Force Fields for simulating material properties.
- Get introduced to Density Functional Theory (DFT) calculations.
- Discuss synthesisability and practical considerations in material synthesis.

**Learning Outcomes:**

- Apply advanced computational methods to materials science problems.
- Integrate thermodynamic principles with machine learning approaches.

---

## Course Objectives

By the end of this course, you will be able to:

- **Generate and Analyze Chemical Spaces:** Efficiently create large chemical composition datasets and analyze them using SMACT.
- **Apply Chemical Filters:** Implement chemical filtering techniques to narrow down potential material candidates.
- **Perform Compositional and Stoichiometry Screening:** Conduct targeted screenings to identify promising materials based on composition and stoichiometry.
- **Utilize Structure Prediction Tools:** Predict and generate crystal structures using SMACT and Chemeleon.
- **Understand Advanced Computational Methods:** Grasp the basics of thermodynamics, Machine Learning Force Fields, DFT, and synthesisability in the context of materials science.
- **Integrate Machine Learning Techniques:** Apply machine learning algorithms to materials informatics workflows.

## Course Format

This is a self-paced practical course built around:

- **Interactive Jupyter Notebooks:** Each topic includes a hands-on notebook with code examples and exercises.
- **Progressive Learning Path:** Starting from basic chemical screening to advanced AI-driven structure generation.
- **Real-World Applications:** Examples drawn from battery materials, solar cells, and other energy applications.
- **Immediate Practice:** Run code locally or in Google Colab to see results in real-time.

## Prerequisites

- **Basic Chemistry Knowledge:** Understanding of chemical formulas, oxidation states, and crystal structures.
- **Python Fundamentals:** Ability to run Python scripts, work with lists/dictionaries, and use basic libraries like NumPy.
- **No ML Experience Required:** We'll introduce machine learning concepts as needed.
- **Curiosity:** Enthusiasm for learning and applying the skills you learn here in your future materials design workflows.

## Materials and Resources

- **SMACT Toolkit:** [github.com/WMD-group/SMACT](https://github.com/WMD-group/SMACT) - Core screening toolkit
- **CHEMELEON:** [github.com/hspark1212/chemeleon-dng](https://github.com/hspark1212/chemeleon-dng) - AI structure generation
- **Materials Project API:** Access to experimental crystal structure data
- **Course Repository:** All notebooks, data files, and setup scripts
- **Key Papers:** Referenced throughout with DOI links for deeper understanding

## How to Use This Course

1. **Start with Setup:** Follow the setup instructions to install all required tools.
2. **Work Through Topics Sequentially:** Each topic builds on the previous ones.
3. **Run All Code Examples:** Understanding comes from doing - run and modify the examples.
4. **Complete the Exercises:** Each notebook includes exercises to reinforce learning.
5. **Explore Your Own Ideas:** Use the tools to investigate materials relevant to your interests.

---

If you have any questions, dont hesitate to reach out and if there's any issues with the notebooks drop Ry an email - napo.nduma22@imperial.ac.uk
