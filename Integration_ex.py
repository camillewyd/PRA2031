class SequenceAnalyzer:
    """A comprehensive DNA sequence analysis tool."""
    
    # Your code here
    def __init__ (self, dna_sequence):
        self.dna_sequence = dna_sequence

    def gc_content(self):
        gc_content = (((self.dna_sequence.count('G')+self.dna_sequence.count('C'))/len(self.dna_sequence))*100)
        return gc_content
    
    def nucleotide_count(self):
        return len(self.dna_sequence)
    
    def transcription(self):
        if 'T' in self.dna_sequence:
            rna_sequence = self.dna_sequence.replace('T','U')
            return rna_sequence
    
    def reverse_complement(self):
        complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
        rev_comp = ''.join(complement[base] for base in reversed(self.dna_sequence))
        return rev_comp
    
    def generate_report(self):
        return f"Summary Report: DNA Sequnence: {self.dna_sequence}, Length: {self.nucleotide_count()}, GC Content: {self.gc_content():.2f}%, RNA Transcription: {self.transcription()}, Reverse Complement: {self.reverse_complement()}"



# Test your class
seq = SequenceAnalyzer("ATGCGATCGATCGTAGCTA")
print(seq.generate_report())