
import json
from codex_widget_factory_lite.visuals.typography import Typography

content = """
<h3 style="background-color:#1E3E5F;font-size:4rem;padding:2rem;display:flex;align-items:center;font-family: Cursive;"><img src="https://cdn.pixabay.com/photo/2017/10/13/15/29/coffee-2847957_640.jpg" alt="img" style="heigh:150px;width:150px;margin-right:2rem"/> displaying some data in table</h3>

| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |


 <h1 style="font-family: Cursive">dispaly some other data</h1>

 Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in\n

1. First item
2. Second item
3. Third item
4. Fourth item

- First item
- Second item
- Third item



# testing this
**testing this** \n
*italic statement*\n
This text is ***really important***
<p style="font-size:1.8rem">~~The world is flat.~~ We now know that the world is round.</p>
I need to highlight these ==very important words==.
<hr style="border-style:dashed"/>

"""
output=Typography(
    content = content
)
output.add_tooltip(isTooltip=True,tooltip_text="This is a tooltip" ,placement="top")
dynamic_outputs = output.json_string
