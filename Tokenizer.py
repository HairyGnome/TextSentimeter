

class Tokenizer:

    def tokenize(self, text):
        # make sure text is utf-8 encoded
        text = text.encode('utf-8')
        tokens = list(map(int, text))

        token_counts = self.count_tokens(tokens)
        top_pair = max(token_counts, key=token_counts.get)

        while token_counts[top_pair] > 1:
            new_token = self.get_token_integer(tokens)
            new_list = []
            for token1, token2 in zip(tokens, tokens[1:]):
                if (token1, token2) == top_pair:
                    new_list.append(new_token)
                else:
                    new_list.append(token1)
            tokens = new_list
            token_counts = self.count_tokens(tokens)
            top_pair = max(token_counts, key=token_counts.get)

        return tokens





    def count_tokens(self, tokens):
        count = {}

        for token1, token2 in zip(tokens, tokens[1:]):
            if (token1, token2) in count:
                count[(token1, token2)] += 1
            else:
                count[(token1, token2)] = 1

        return count


    def get_token_integer(self, tokens):
        for i in range(256):
            if i not in tokens:
                return i
        return 255


if __name__ == '__main__':
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize('Hello Hello HIHIHI')
    print(tokens)
