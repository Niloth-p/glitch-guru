# Source environment variables (PROJECT_DIR) from settings_local.py
source GlitchGuru/settings_local.py

SOURCE_BRANCH="main"
BACKUP_BRANCH="backup"

cd "$PROJECT_DIR"

# Create or switch to the backup branch
if ! git show-ref --verify --quiet "refs/heads/$BACKUP_BRANCH"; then
    git checkout -b "$BACKUP_BRANCH"
else
    git checkout "$BACKUP_BRANCH"
fi

# Commit and push all changes in the project directory with a timestamped message
TIMESTAMP=$(date +'%Y-%m-%d %H:%M:%S')
git add .
git commit -m "Backup: $TIMESTAMP"
git push origin "$BACKUP_BRANCH"

git checkout "$SOURCE_BRANCH"
echo "Backup completed and pushed to branch '$BACKUP_BRANCH' with timestamp $TIMESTAMP."
