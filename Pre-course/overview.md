# Introduction to the Course

Welcome to the **"Fundamentals of Machine Learning and AI for Materials Exploration"** course! This course is designed for incoming students eager to delve into the exciting intersection of materials science, machine learning, and artificial intelligence. You will learn how to leverage computational tools to accelerate the discovery of new materials, focusing primarily on the **SMACT (Semiconducting Materials from Analogy and Chemical Theory)** toolkit. SMACT offers a collection of rapid screening and informatics tools utilizing chemical element data to facilitate materials exploration.

# Course Overview

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

### 5.2 Crystal Structure Generation with Chemeleon

**Description:**
- Explore **Chemeleon**, a text-guided diffusion model for crystal structure generation.
- Generate crystal structures using natural language descriptions or specified compositions.
- Compare Chemeleon's outputs with those from SMACT's structure prediction module.

**Learning Outcomes:**
- Use AI-driven tools for crystal structure generation.
- Evaluate different structure prediction methodologies.

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

# Course Objectives

By the end of this course, you will be able to:

- **Generate and Analyze Chemical Spaces:** Efficiently create large chemical composition datasets and analyze them using SMACT.
- **Apply Chemical Filters:** Implement chemical filtering techniques to narrow down potential material candidates.
- **Perform Compositional and Stoichiometry Screening:** Conduct targeted screenings to identify promising materials based on composition and stoichiometry.
- **Utilize Structure Prediction Tools:** Predict and generate crystal structures using SMACT and Chemeleon.
- **Understand Advanced Computational Methods:** Grasp the basics of thermodynamics, Machine Learning Force Fields, DFT, and synthesisability in the context of materials science.
- **Integrate Machine Learning Techniques:** Apply machine learning algorithms to materials informatics workflows.

# Course Format

- **Lectures:** Conceptual understanding of machine learning and materials informatics.
- **Hands-on Coding Sessions:** Practical exercises using SMACT (and Chemeleon).
- **Interactive Notebooks:** Step-by-step guides to reinforce learning through application.
- **Discussions:** Collaborative problem-solving and knowledge sharing.

# Prerequisites

- **Basic Chemistry and Materials Science Knowledge:** Understanding of elemental properties and material structures.
- **Python Programming:** Familiarity with Python programming for hands-on sessions.
- **Interest in AI Applications:** Enthusiasm for exploring AI and machine learning in materials science.

# Materials and Resources

- **SMACT Toolkit Documentation:** Guides and tutorials for using SMACT.
- **Chemeleon Access:** Tools for crystal structure generation.
- **Supplementary Readings:** Articles and papers on machine learning and materials informatics.
- **Interactive Notebooks:** Pre-prepared coding environments for practical exercises.

# Assessment

- **Participation:** Active involvement in lectures and hands-on sessions.
- **Assignments:** Regular tasks to apply concepts learned.
- **Projects:** A final project involving the application of course concepts to a materials discovery problem.

---

We look forward to guiding you through this exciting journey at the forefront of materials science and artificial intelligence. Let's embark on the path to discovering new materials together!