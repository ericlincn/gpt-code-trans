from io import BytesIO
import tokenize

class StringUtil:

    @staticmethod
    def findLastNewlinePosition(contentAsBytes, threshold:int) -> list[int]:
        tokens = tokenize.tokenize(BytesIO(contentAsBytes).readline)
        tokenCount = 0
        tokenRow = 0
        tokenRows = []
        for token in tokens:
                
                # the line is contains only whitespace characters, and not header/fotter lines
                if all(c.isspace() for c in token.line) and (token.start[1] + token.end[1]) != 0:
                    # print(token.start, token.end, tokenCount, "Token contains only whitespace characters")
                    tokenRow = token.start[0]
                tokenCount += 1

                if tokenCount > threshold:
                    tokenRows.append(tokenRow)
                    tokenCount = 0

        return tokenRows

    @staticmethod
    def splitFromRows(content: str, rows: list[int]) -> list[str]:
        text_lines = content.split("\n")
        parts = []
        start = 0
        for row in rows:
            parts.append("\n".join(text_lines[start:row - 1]))
            start = row
        parts.append("\n".join(text_lines[start:]))
        return parts