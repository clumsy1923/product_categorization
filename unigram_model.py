class unigram_model:
    def __init__(self, category, vocab_size):
        self.category = category
        self.probs = {}
        for i in range(vocab_size):
            self.probs[i+1]=float(0.000001)
    def add_word_entity(self, index):
        self.probs[index]+=float(1)
    def normalize_probs(self):
        count=0
        for key in self.probs.keys():
            count+=self.probs[key]
        for key in self.probs.keys():
            self.probs[key]/=count
    def get_sequence_probability(self, sequence):
        p = 1.0
        for word in sequence:
            if word in self.probs:
                p*=self.probs[word]
        return p
