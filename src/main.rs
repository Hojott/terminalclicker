use std::io::{self,Write};

struct Command {
    keyword : String,
    args : Vec<String>
}

fn print_prompt(ps: &str) {
    print!("{0} ", ps);
    io::stdout().flush().unwrap();
}

fn read_command() -> String {
    let mut command = String::new();
    io::stdin().read_line(&mut command)
        .expect("Failed to read in command");
    
    command
}

fn tokenize_command(input: String) -> Command {
    let mut command_split : Vec<String> = input.split_whitespace().map(|s| s.to_string()).collect();
    
    let command = Command {
        keyword : command_split.remove(0),
        args : command_split,
    };

    command
}

fn main() {
    let prompt = ">";
    loop {    
        print_prompt(prompt);

        let input = read_command();
        let command = tokenize_command(input);
        
        println!("DEBUG {0} {1:?}", command.keyword, command.args);
    }
}


#[cfg(test)]
mod unittest_tokenize_command {
    use super::*;

    #[test]
    #[ignore]
    fn empty_command() {
        assert_eq!("", tokenize_command("".to_string()).keyword)
    }

    #[test]
    fn test_keyword() {
      assert_eq!("test", tokenize_command("test".to_string()).keyword)
    }

    #[test]
    fn no_arg() {
      assert_eq!(0, tokenize_command("test".to_string()).args.len())
    }

    #[test]
    fn one_arg() {
      assert_eq!(1, tokenize_command("test one".to_string()).args.len())
    }

    #[test]
    fn multi_args() {
      assert_eq!(3, tokenize_command("test one two three".to_string()).args.len())
    }

    #[test]
    #[ignore]
    fn quotes() {
      assert_eq!(2, tokenize_command("test \"one two\" three".to_string()).args.len())
    }
}