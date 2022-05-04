
class Code():
    def __init__(self, line, extra_lines=[]) -> None:
        self.line = line
        if extra_lines:
            for inline in extra_lines:
                if isinstance(inline, CodeBreak):
                    self.line += ("\n" * inline.line_break)
                elif isinstance(inline, (CodeBlock, Code)):
                    self.line += f"{inline.__str__()}\n"
                else:
                    self.line += f"{inline}\n"

    def __str__(self) -> str:
        return f"{self.line}"

    def __add__(self, obj2) -> str:
        if isinstance(obj2, (CodeBreak)):
            result = Code(f"{self.line}" + ("\n" * obj2.line_break))
        elif isinstance(obj2, (CodeBlock)):
            result = Code(f"{self.line}" + "\n" + obj2.__str__())
        elif isinstance(obj2, (Code)):
            result = Code(f"{self.line}\n{obj2.line}")
        else:
            result = Code(f"{self.line}\n{obj2}")
        return result


class CodeBreak():
    def __init__(self, line_break=2) -> None:
        self.line_break = line_break


class CodeBlock():
    def __init__(self, head, block):
        self.head = head
        self.block = block

    def __str__(self, indent=""):
        result = indent + self.head + ":\n"
        indent += "    "
        for block in self.block:
            if isinstance(block, CodeBlock):
                result += block.__str__(indent)
            elif isinstance(block, Code):
                result += indent + f"{block.__str__()}\n"
            elif isinstance(block, CodeBreak):
                result += "\n" * block.line_break
            else:
                result += indent + block + "\n"
        return result
