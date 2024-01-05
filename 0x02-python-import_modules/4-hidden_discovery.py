#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    [
            print(i)
            for i in dir(hidden_4)
            if not i.startswith('__')
    ]
