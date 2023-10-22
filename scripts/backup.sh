source .env

SOURCE_BRANCH="main"
BACKUP_BRANCH="backup"

# Create or switch to the backup branch
if ! git show-ref --verify --quiet "refs/heads/$BACKUP_BRANCH"; then
    git checkout -b "$BACKUP_BRANCH"
else
    git checkout "$BACKUP_BRANCH"
fi
echo "Checked out the backup branch."

# Commit and push all changes in the project directory with a timestamped message
git commit -m "Backup: $(date +'%Y-%m-%d %H:%M:%S')"
echo "Committed once"
if [[ -n $(git status -s) ]]; then
    git add .
    git commit -m "Backup: $(date +'%Y-%m-%d %H:%M:%S')"
    echo "Committed twice"
fi
git push origin "$BACKUP_BRANCH"

git checkout "$SOURCE_BRANCH"
echo "Backup completed and pushed to branch '$BACKUP_BRANCH' with timestamp $TIMESTAMP."
