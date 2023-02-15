(*
   AST and matching of a glob pattern against a path.
   This is purely syntaxic: the file system is not accessed.
*)

(* The location of a pattern, for logging and troubleshooting. *)
type loc = {
  (* File name or other source location name useful to a human reader
     in error messages. *)
  source_name : string;
  (* Line number, starting from 1. *)
  line_number : int;
  line_contents : string;
}

type char_class_range = Class_char of char | Range of char * char
type char_class = { complement : bool; ranges : char_class_range list }

type component_fragment =
  | Char of char
  | Char_class of char_class
  | Question
  | Star

(* A path component is what represents a simple file name in a directory *)
type component =
  | Component of component_fragment list
  | Ellipsis (* '**' = path ellipsis *)

(*
   A pattern which matches paths.
*)
type pattern = component list

(* A compiled pattern matcher. *)
type compiled_pattern

(* The pattern that matches '/' *)
val root_pattern : pattern

(*
   Compile the pattern into something efficient. The source should be
   the original glob pattern before parsing. It's used only for debugging
   purposes.
*)
val compile : source:loc -> pattern -> compiled_pattern

(*
   Match a path against a pattern:
   - The path must be slash-separated (not backslash-separated like on
     Windows).
   - If the pattern starts with a slash, the path must start with a slash
     as well. In both cases, the matching starts from the beginning.
   - Matching is purely syntactic. No file system lookup will be attempted.

   Examples:

   absolute pattern: /*.c
   matching paths: /foo.c /bar.c
   non-matching paths: foo.c bar.c /tmp/foo.c /tmp/bar.c

   relative pattern: *.c
   matching paths: bar.c
   non-matching paths: /bar.c foo.c/bar bar/foo.c

   sliding pattern: **/.c
   matching paths: foo.c bar/foo.c /foo.c
   non-matching paths: foo.c/bar

   folder pattern: foo/
   matching paths: foo/
   non-matching paths: foo bar/foo/ /foo/ /foo
*)
val run : compiled_pattern -> string -> bool

val source : compiled_pattern -> loc

val of_path_components : string list -> pattern
