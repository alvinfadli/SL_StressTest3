# Number 3 (Pattern Scaling)

Question number 3 for SL Stress Test

#### References :

I use this formula to calculate the starting position of the inner rectangle :

X = Cx + (r x cosine(angle))  
Y = Cy + (r x sine(angle))

Source : https://stackoverflow.com/questions/14096138/find-the-point-on-a-circle-with-given-center-point-radius-and-degree

Follow this step to run the program, let me know if there is a problem while setup or running the code

## Project Setup

#### Create virtual environment

```bash
  python -m venv venv
```

#### Activate virtual environment

On windows

```bash
  .\venv\Scripts\activate

```

On linux

```bash
  source venv/Scripts/activate
```

#### Install dependencies

```bash
  pip install -r requirements.txt
```

## Running

Total can be modified based on the flags

example for 10 pattern :

```bash
  python main.py -total=10
```

example for 500 pattern :

```bash
  python main.py -total=500
```
