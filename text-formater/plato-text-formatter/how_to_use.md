# how to use

```py
formatter = PlatoTextFormatter()

text = "Hello 😅\nThis is line 2\nLine 3\nLine 4 🐱‍👤"

# Strict mode: will raise error if too long or too many lines
try:
    result = formatter.strict_format(text)
except FormatError as e:
    print("Error:", e)

# Soft mode: trims to 3 lines and max 255 chars
result_soft = formatter.soft_format(text)
print("Soft formatted text:\n", result_soft)

# Preview
preview = formatter.preview(text)
print("Plato preview:\n", preview)
```
