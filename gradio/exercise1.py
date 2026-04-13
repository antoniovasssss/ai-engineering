# Adding share=True means that it can be accessed publically
# A more permanent hosting is available using a platform called Spaces from HuggingFace,
# NOTE: Some Anti-virus software and Corporate Firewalls might not like you using share=True. 
# If you're at work on on a work network, I suggest skip this test.


import gradio as gr

# pip install --upgrade gradio
def greet(text):
    print(f"Shout has been called with input {text}")
    return text.upper()

greet("example text")



gr.Interface(fn=greet, inputs="textbox", outputs="textbox", flagging_mode="never").launch(share=True)

# Adding inbrowser=True opens up a new browser window automatically

gr.Interface(fn=greet, inputs="textbox", outputs="textbox", flagging_mode="never").launch(inbrowser=True)

# Define this variable and then pass js=force_dark_mode when creating the Interface

force_dark_mode = """
function refresh() {
    const url = new URL(window.location);
    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""
gr.Interface(fn=greet, inputs="textbox", outputs="textbox", flagging_mode="never", js=force_dark_mode).launch()

message_input = gr.Textbox(label="Your message:", info="Enter a message to be greeted", lines=7)
message_output = gr.Textbox(label="Response:", lines=8)

view = gr.Interface(
    fn=greet,
    title="Greet", 
    inputs=[message_input], 
    outputs=[message_output], 
    examples=["hello", "howdy"], 
    flagging_mode="never"
    )
view.launch()