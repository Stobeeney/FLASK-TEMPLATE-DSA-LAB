from flask import Flask, render_template, request
from queue_link_list import Queue
from input_restricted_deque import InputRestrictedDeque
from output_restricted_deque import OutputRestrictedDeque
from stack import infix_to_postfix


app = Flask(__name__)


# INITIALIZATIONS

linked_list_data = []

postfix_steps = []

queue = Queue()
inputrestricted = InputRestrictedDeque()
outputrestricted = OutputRestrictedDeque()

# LOGIN

@app.route('/')
def login():
    return render_template('login.html')


# HOMEPAGE

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/artist_homepage')
def artist_homepage():
    return render_template('artist_homepage.html')


# PROFILES

@app.route('/daniel')
def daniel():
    return render_template('daniel.html')

@app.route('/april')
def april():
    return render_template('april.html')

@app.route('/celine')
def celine():
    return render_template('celine.html')

@app.route('/jamaica')
def jamaica():
    return render_template('jamaica.html')

@app.route('/godwin')
def godwin():
    return render_template('godwin.html')

@app.route('/jester')
def jester():
    return render_template('jester.html')

@app.route('/glenn')
def glenn():
    return render_template('glenn.html')


# LINKED LIST

@app.route('/linked_list', methods=['GET', 'POST'])
def linked_list():
    message = None
    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value')

        if action == 'insert_beginning':
            if value:
                linked_list_data.insert(0, value)
                message = f"Inserted {value} at the beginning."
            else:
                message = "Please enter an element to insert."

        elif action == 'insert_end':
            if value:
                linked_list_data.append(value)
                message = f"Inserted {value} at the end."
            else:
                message = "Please enter an element to insert."

        elif action == 'delete_beginning':
            if linked_list_data:
                removed = linked_list_data.pop(0)
                message = f"Removed {removed} from the beginning."
            else:
                message = "No elements in the list to remove."

        elif action == 'delete_end':
            if linked_list_data:
                removed = linked_list_data.pop()
                message = f"Removed {removed} from the end."
            else:
                message = "No elements in the list to remove."

        elif action == 'delete_at':
            if value.isdigit():
                index = int(value)
                if 0 <= index < len(linked_list_data):
                    removed = linked_list_data.pop(index)
                    message = f"Removed {removed} at index {index}."
                else:
                    message = "Invalid index. Please enter a valid index to remove."
            else:
                message = "Please enter an index to remove."

        elif action == 'search':
            if value:
                if value in linked_list_data:
                    index = linked_list_data.index(value)
                    message = f"{value} found at index {index} in the list."
                else:
                    message = f"{value} not found in the list."
            else:
                message = "Please enter an element to search."

    return render_template('linked_list.html', linked_list=linked_list_data, message=message)


# STACK

@app.route("/stack", methods=["GET", "POST"])
def stack():
    global postfix_steps
    output = None
    message = None
    infix_expression = None 

    if request.method == "POST":
        action = request.form.get("action")

        if action == "push":
            infix_expression = request.form.get("infix", "").strip()
            if infix_expression: 
                postfix_steps = infix_to_postfix(infix_expression)
                output = "".join(postfix_steps[-1]) if postfix_steps else None
                message = "Conversion successful!" 
            else:
                message = "Please enter a valid infix expression."
        elif action == "clear":
            
            postfix_steps = []
            output = None
            message = "Stack cleared."

    return render_template("stack.html", postfix_steps=postfix_steps, output=output, message=message, infix_expression=infix_expression)


# QUEUE

@app.route('/overall_choose')
def overall_choose():
    return render_template('overall_choose.html')

@app.route('/deque_choose')
def deque_choose():
    return render_template('deque_choose.html')

@app.route('/queue', methods=['GET', 'POST'])
def queue_operations():

    message = None

    if request.method == 'POST':
        action = request.form['action']
        value = request.form.get('value', '').strip()

        if action == 'enqueue':
            if value:
                queue.enqueue(value)
                message = f'"{value}" enqueued.'
            else:
                message = 'Please provide a value to enqueue.'
        elif action == 'dequeue':
            dequeued_value = queue.dequeue()
            if dequeued_value:
                message = f'Dequeued value: "{dequeued_value}".'
            else:
                message = 'Queue is empty. Nothing to dequeue.'

    return render_template('queue.html', queue=list(queue), message=message)


@app.route('/input_restricted_deque', methods=['GET', 'POST'])
def input_restricted_deque_operations():
    message = None

    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value', '').strip()

        if action == 'enqueue_at_end':
            if value:
                inputrestricted.enqueue_at_end(value)
                message = f'"{value}" enqueued.'
            else:
                message = 'Please provide a value to enqueue.'
    
        elif action == 'dequeue_at_beginning':
            dequeued_head_value = inputrestricted.dequeue_at_beginning()
            if dequeued_head_value:
                message = f'Dequeued value: "{dequeued_head_value}".'
            else:
                message = 'Queue is empty. Nothing to dequeue.'

        elif action == 'dequeue_at_end':
            dequeued_tail_value = inputrestricted.dequeue_at_end()
            if dequeued_tail_value:
                message = f'Dequeued value: "{dequeued_tail_value}".'
            else:
                message = 'Queue is empty. Nothing to dequeue.'

    return render_template('input_deque.html', inputrestricted=list(inputrestricted), message=message)


@app.route('/output_restricted_deque', methods=['GET', 'POST'])
def output_restricted_deque_operations():
    message = None

    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value', '').strip()

        if action == 'enqueue_at_end':
            if value:
                outputrestricted.enqueue_at_end(value)
                message = f'"{value}" enqueued.'
            else:
                message = 'Please provide a value to enqueue.'

        elif action == 'enqueue_at_beginning':
            if value:
                outputrestricted.enqueue_at_beginning(value)
                message = f'"{value} enqueued.'
            else:
                message = 'Please provide a value to enqueue'

        elif action == 'dequeue_at_beginning':
            dequeued_head_value = outputrestricted.dequeue_at_beginning()
            if dequeued_head_value:
                message = f'Dequeued value: "{dequeued_head_value}".'
            else:
                message = 'Queue is empty. Nothing to dequeue.'            

    return render_template('output_deque.html', outputrestricted=list(outputrestricted), message=message)


if __name__ == '__main__':
    app.run(debug=True)

print(app.jinja_loader.searchpath)
