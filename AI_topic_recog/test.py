def main():
    # Use a pipeline as a high-level helper
    from transformers import pipeline

    pipe = pipeline("text-classification", model="oracat/bert-paper-classifier-arxiv")


    output = pipe("The Ginzburg Landau theory for d_{x^2-y^2}-wave superconductors is constructed, by starting from the Gor'kov equation with including correction terms up to the next order of ln(T_c/T). Some of the non-local correction terms are found to break the cylindrical symmetry and lead to the fourfold symmetric core structure, reflecting the internal degree of freedom in the pair potential. Using this extended Ginzburg Landau theory, we investigate the fourfold symmetric structure of the pair potential, current and magnetic field around an isolated single vortex, and clarify concretely how the vortex core structure deviates from the cylindrical symmetry in the d_{x^2-y^2}-wave superconductors.")
    print(output)
    
if __name__ == '__main__':
    main()