"""
Plato Text Formatter Module
---------------------------

This module is optimized for PlatoApp messages. It handles:
1. Correct character counting for emojis (UTF-16 style)
2. Max total characters (255)
3. Max real lines (3)
4. Trimming or error-raising
5. Optional preview of how the message would appear

Author: Ehsan
Repo: python-playground
"""

class FormatError(Exception):
    """Raised when Plato text formatting rules are violated."""
    pass

class PlatoTextFormatter:
    def __init__(self, max_chars=255, max_lines=3):
        self.max_chars = max_chars
        self.max_lines = max_lines

    @staticmethod
    def _plato_char_count(text: str) -> int:
        """
        Counts text in a way Plato does:
        - Every emoji (surrogate pair) counts as 2
        - Other characters count as 1
        """
        count = 0
        for c in text:
            # Unicode surrogate pairs: code points > U+FFFF
            if ord(c) > 0xFFFF:
                count += 2
            else:
                count += 1
        return count

    def strict_format(self, text: str) -> str:
        """
        Validate text and raise FormatError if it exceeds Plato limits
        """
        char_count = self._plato_char_count(text)
        if char_count > self.max_chars:
            raise FormatError(f"Text exceeds Plato max of {self.max_chars} chars (current {char_count})")

        lines = text.split("\n")
        if len(lines) > self.max_lines:
            raise FormatError(f"Text exceeds Plato max of {self.max_lines} lines (current {len(lines)})")

        return text

    def soft_format(self, text: str) -> str:
        """
        Trim text to fit Plato rules:
        - Trims characters to max_chars
        - Trims extra lines to max_lines
        """
        # Trim lines first
        lines = text.split("\n")[:self.max_lines]

        # Rebuild text
        text = "\n".join(lines)

        # Trim characters respecting Plato emoji count
        trimmed = ""
        count = 0
        for c in text:
            c_len = 2 if ord(c) > 0xFFFF else 1
            if count + c_len > self.max_chars:
                break
            trimmed += c
            count += c_len

        return trimmed

    def preview(self, text: str) -> str:
        """
        Shows a preview of how text will appear in Plato:
        - Max 3 lines
        - No hard wrapping added
        """
        lines = text.split("\n")[:self.max_lines]
        return "\n".join(lines)

