# Machine Learning Force Fields

This section explores the application of machine learning techniques to develop accurate and efficient interatomic force fields for materials simulation.

For your reference here's the MACE repository: [ACEsuit/mace](https://github.com/ACEsuit/mace).

## Learning Objectives

After completing this section, you will be able to:

1. Understand the principles behind machine learning force fields
2. Compare different ML approaches for force field development
3. Evaluate the accuracy and transferability of ML force fields
4. Apply ML force fields to materials problems

## Topics Covered

1. Fundamentals of Force Fields
   - Classical Force Fields
   - Quantum Mechanical Reference Data
   - Machine Learning Approaches

2. Types of ML Force Fields
   - Neural Network Potentials
   - Gaussian Process Regression
   - Kernel Methods
   - Deep Learning Models

3. Applications
   - Molecular Dynamics
   - Structure Prediction
   - Property Prediction
   - High-Throughput Screening

## Available Resources

### MACE (Multi-Atomic Cluster Expansion)

We provide comprehensive documentation for MACE, a state-of-the-art machine learning force field:

- **[MACE Tutorial](mace_tutorial.md)**: Step-by-step guide to installation, usage, and training
- **[MACE Theory](mace_theory.md)**: Deep dive into the theoretical foundations and architecture

These resources will help you understand and apply modern machine learning force fields to accelerate your materials research.

### References

```bibtex
@inproceedings{Batatia2022mace,
  title={{MACE}: Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields},
  author={Ilyes Batatia and David Peter Kovacs and Gregor N. C. Simm and Christoph Ortner and Gabor Csanyi},
  booktitle={Advances in Neural Information Processing Systems},
  editor={Alice H. Oh and Alekh Agarwal and Danielle Belgrave and Kyunghyun Cho},
  year={2022},
  url={https://openreview.net/forum?id=YPpSngE-ZU}
}

@misc{Batatia2022Design,
  title = {The Design Space of E(3)-Equivariant Atom-Centered Interatomic Potentials},
  author = {Batatia, Ilyes and Batzner, Simon and Kov{\'a}cs, D{\'a}vid P{\'e}ter and Musaelian, Albert and Simm, Gregor N. C. and Drautz, Ralf and Ortner, Christoph and Kozinsky, Boris and Cs{\'a}nyi, G{\'a}bor},
  year = {2022},
  number = {arXiv:2205.06643},
  eprint = {2205.06643},
  eprinttype = {arxiv},
  doi = {10.48550/arXiv.2205.06643},
  archiveprefix = {arXiv}
 }
```
