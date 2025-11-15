# Python Playground

A collection of Python utilities, text formatting tools, and common code snippets for learning and reference.

## 📁 Project Structure

#### `text-formater/plato-text-formatter/`

Plato Text Formatter module for handling message formatting with Plato app constraints.

**Features:**

- UTF-16 style emoji character counting (emojis count as 2 characters)
- Max character limit: 255
- Max lines limit: 3
- Two formatting modes: strict (validates) and soft (trims)
- Preview functionality

**Files:**

- [`plato_text_formatter.py`](text-formater/plato-text-formatter/plato_text_formatter.py) - Main formatter class
- [`how_to_use.md`](text-formater/plato-text-formatter/how_to_use.md) - Usage examples

---

#### `proccessing-utils/`

Image and file processing utilities.

**Files:**

- [`image_pre-proccessing.py`](proccessing-utils/image_pre-proccessing.py)
  - Decode base64 to PIL Image
  - Handle EXIF image rotation
  - Encode images/arrays to base64
  - Resize and crop images
  - Save images to temporary files

- [`general.py`](proccessing-utils/general.py)
  - Convert binary/dictionary to bytes
  - Encode URLs or files to base64
  - Validate URLs
  - MIME type detection

- [`encryptor.py`](proccessing-utils/encryptor.py)
  - AES encryption/decryption with CBC mode
  - Key generation from passwords
  - Automatic padding handling
  - *Originated from [Gradio](https://github.com/gradio-app/gradio)*

---

#### `common-snippets/`

Reusable code snippets organized by difficulty level.

#### Part 1 - Basics

- [`iindex-for-loop.py`](common-snippets/part-1/iindex-for-loop.py) - Access list indices with enumeration
- [`generate-captcha.py`](common-snippets/part-1/generate-captcha.py) - Generate CAPTCHA images
- [`shuffle-a-deck.py`](common-snippets/part-1/shuffle-a-deck.py) - Shuffle and draw card deck
- [`prime.number.py`](common-snippets/part-1/prime.number.py) - Check if number is prime
- [`countdown-time.py`](common-snippets/part-1/countdown-time.py) - Display countdown timer

#### Part 2 - Intermediate

- [`chcek_palindrome.py`](common-snippets/part-2/chcek_palindrome.py) - Check if string is palindrome
- [`while-loop.py`](common-snippets/part-2/while-loop.py) - While loop examples
- [`fizz-buzz.py`](common-snippets/part-2/fizz-buzz.py) - FizzBuzz problem solution
- [`list.py`](common-snippets/part-2/list.py) - List operations and methods
- [`boolean-logic.py`](common-snippets/part-2/boolean-logic.py) - Boolean condition examples
- [`Transpose-a-Matrix.py`](common-snippets/part-2/Transpose-a-Matrix.py) - Matrix transposition methods
- [`Chaining-Multiple-Conditions.py`](common-snippets/part-2/Chaining-Multiple-Conditions.py) - Complex boolean logic
- [`req.py`](common-snippets/part-2/req.py) - Socket-based HTTP requests
- [`get-request-loop.py`](common-snippets/part-2/get-request-loop.py) - HTTP GET requests with redirects

#### Part 3 - Advanced

- [`extract-file-extension.py`](common-snippets/part-3/extract-file-extension.py) - Extract file extensions
- [`merge-mails.py`](common-snippets/part-3/merge-mails.py) - Merge mail templates with names
- [`find-hash.py`](common-snippets/part-3/find-hash.py) - Calculate SHA-1 file hash

---
