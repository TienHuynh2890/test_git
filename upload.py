import subprocess

def git_auto_push():
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", "update code"],
        ["git", "push"]
    ]
    
    for cmd in commands:
        print(f"Đang chạy: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # In kết quả trả về từ lệnh git
        if result.stdout:
            print(result.stdout)
        
        # Nếu có lỗi (returncode khác 0), dừng lại và báo lỗi
        if result.returncode != 0:
            print(f"Lỗi: {result.stderr}")
            break
    else:
        print("Đã hoàn tất push code thành công")

if __name__ == "__main__":
    git_auto_push()