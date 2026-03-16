import re
import sys

def validate_commit_message(message):
    """
    Validates the commit message against the Conventional Commits specification.
    Format: <type>(<scope>): <emoji> <subject>
    """
    # Regex pattern for the header
    # Supports optional scope, optional emoji
    # Type must be one of the standard types
    types = r"feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert"
    pattern = fr"^({types})(\(.+\))?: (?:.|[\u2700-\u27BF]|(?:\ud83c[\udde6-\uddff]){{2}}|[\ud800-\udbff][\udc00-\udfff]|[\u0023-\u0039]\ufe0f?\u20e3|\u3299|\u3297|\u303d|\u3030|\u24c2|\ud83c[\udd70-\udd71]|\ud83c[\udd7e-\udd7f]|\ud83c\udd8e|\ud83c[\udd91-\udd9a]|\ud83c[\udde6-\uddff]|\ud83c[\ude01-\ude02]|\ud83c\ude1a|\ud83c\ude2f|\ud83c[\ude32-\ude3a]|\ud83c[\ude50-\ude51]|\u203c|\u2049|[\u25aa-\u25ab]|\u25b6|\u25c0|[\u25fb-\u25fe]|\u00a9|\u00ae|\u2122|\u2139|\ud83c\udc04|[\u2600-\u26FF]|\u2b05|\u2b06|\u2b07|\u2b1b|\u2b1c|\u2b50|\u2b55|\u231a|\u231b|\u2328|\u23cf|[\u23e9-\u23f3]|[\u23f8-\u23fa]|\ud83c\udccf|\u2934|\u2935|[\u2190-\u21ff])? ?(.+)$"
    
    lines = message.strip().split('\n')
    header = lines[0]
    
    if not re.match(pattern, header):
        print(f"Error: Header does not match Conventional Commits format.\nHeader: {header}")
        return False
        
    # Check for empty line after header if body exists
    if len(lines) > 1 and lines[1].strip() != "":
        print("Error: Body must be separated from header by a blank line.")
        return False
        
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate.py <commit_message>")
        sys.exit(1)
        
    msg = sys.argv[1]
    if validate_commit_message(msg):
        print("Commit message is valid.")
        sys.exit(0)
    else:
        sys.exit(1)
