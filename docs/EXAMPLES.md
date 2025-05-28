# BlueSky Followers Utility - Examples

This document provides comprehensive examples for using the BlueSky Followers Utility v2.0.0.

## Table of Contents

1. [Basic Library Usage](#basic-library-usage)
2. [CLI Usage](#cli-usage)
3. [Data Analysis Examples](#data-analysis-examples)
4. [Error Handling](#error-handling)
5. [Integration Examples](#integration-examples)
6. [Advanced Usage](#advanced-usage)

## Basic Library Usage

### Simple Follower Retrieval

```python
from bluesky_util import BlueSkyFollowers

# Initialize the client
bf = BlueSkyFollowers()

# Get followers for a user
data = bf.get_followers_data('jack.bsky.social', limit=50)

if data['success']:
    print(f"Found {len(data['followers'])} followers for @{data['username']}")
    
    # Show first 5 followers
    for i, follower in enumerate(data['followers'][:5], 1):
        print(f"{i}. @{follower['handle']} - {follower['display_name']}")
else:
    print(f"Error: {data['error']}")
```

### Display Formatted Table

```python
from bluesky_util import BlueSkyFollowers

bf = BlueSkyFollowers()

# Display followers in a beautiful table
success = bf.display_followers_table('jack.bsky.social', limit=25)

if success:
    print("✓ Successfully displayed followers")
else:
    print("✗ Failed to display followers")
```

### Profile Information

```python
from bluesky_util import BlueSkyFollowers

bf = BlueSkyFollowers()

# Get user profile
profile = bf.get_user_profile('jack.bsky.social')

if profile:
    print(f"User: {profile.display_name}")
    print(f"Handle: @{profile.handle}")
    print(f"Description: {profile.description}")
    print(f"Followers: {profile.followers_count}")
    print(f"Following: {profile.follows_count}")
else:
    print("User not found")
```

## CLI Usage

### Basic Commands

```bash
# Get followers (default limit: 100)
python cli.py jack.bsky.social

# Specify custom limit
python cli.py jack.bsky.social --limit 50

# Hide description column
python cli.py jack.bsky.social --limit 25 --no-description

# Using uv
uv run python cli.py jack.bsky.social --limit 30
```

### Help and Version

```bash
# Get help
python cli.py --help

# Check version
python cli.py --version
```

### Custom Domains

```bash
# Works with any custom domain
python cli.py user.example.com --limit 50
python cli.py someone.custom-domain.org --limit 100
```

## Data Analysis Examples

### Follower Growth Analysis

```python
from bluesky_util import BlueSkyFollowers
from collections import defaultdict
import json

bf = BlueSkyFollowers()

def analyze_follower_growth(username, limit=500):
    """Analyze when followers joined BlueSky"""
    data = bf.get_followers_data(username, limit=limit)
    
    if not data['success']:
        print(f"Error: {data['error']}")
        return
    
    # Group by year/month
    growth_by_month = defaultdict(int)
    
    for follower in data['followers']:
        joined_date = follower['joined_date_raw']
        if joined_date:
            # Extract year-month from ISO date
            month = joined_date[:7]  # YYYY-MM
            growth_by_month[month] += 1
    
    # Sort by date
    sorted_growth = sorted(growth_by_month.items())
    
    print(f"Follower Growth Analysis for @{username}")
    print("=" * 50)
    
    total = 0
    for month, count in sorted_growth:
        total += count
        print(f"{month}: {count:3d} new followers (total: {total})")
    
    return sorted_growth

# Example usage
growth = analyze_follower_growth('jack.bsky.social', limit=200)
```

### Export to JSON

```python
from bluesky_util import BlueSkyFollowers
import json
from datetime import datetime

bf = BlueSkyFollowers()

def export_followers_json(username, filename=None, limit=100):
    """Export follower data to JSON file"""
    data = bf.get_followers_data(username, limit=limit)
    
    if not data['success']:
        print(f"Error: {data['error']}")
        return False
    
    # Add export metadata
    export_data = {
        "export_info": {
            "exported_at": datetime.now().isoformat(),
            "username": username,
            "total_exported": len(data['followers']),
            "limit_requested": limit
        },
        "target_user": data['target_user'],
        "followers": data['followers']
    }
    
    # Generate filename if not provided
    if not filename:
        safe_username = username.replace('.', '_')
        filename = f"followers_{safe_username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Exported {len(data['followers'])} followers to {filename}")
    return True

# Example usage
export_followers_json('jack.bsky.social', limit=100)
```

### Compare Multiple Users

```python
from bluesky_util import BlueSkyFollowers
import time

bf = BlueSkyFollowers()

def compare_users(usernames, limit=50):
    """Compare follower counts and growth for multiple users"""
    results = {}
    
    for username in usernames:
        print(f"Analyzing @{username}...")
        
        data = bf.get_followers_data(username, limit=limit)
        
        if data['success']:
            target = data['target_user']
            followers = data['followers']
            
            # Calculate average join time (days since BlueSky launch)
            join_dates = [f['joined_date_raw'] for f in followers if f['joined_date_raw']]
            
            results[username] = {
                'display_name': target['display_name'],
                'total_followers': target['follower_count'],
                'total_following': target['following_count'],
                'analyzed_followers': len(followers),
                'join_dates_available': len(join_dates)
            }
        else:
            results[username] = {'error': data['error']}
        
        # Be respectful to the API
        time.sleep(1)
    
    # Display comparison
    print("\nUser Comparison")
    print("=" * 80)
    print(f"{'Username':<25} {'Display Name':<20} {'Followers':<10} {'Following':<10}")
    print("-" * 80)
    
    for username, info in results.items():
        if 'error' not in info:
            print(f"{username:<25} {info['display_name']:<20} {info['total_followers']:<10} {info['total_following']:<10}")
        else:
            print(f"{username:<25} ERROR: {info['error']}")
    
    return results

# Example usage
users = ['jack.bsky.social', 'pfrazee.com', 'jay.bsky.social']
comparison = compare_users(users, limit=30)
```

## Error Handling

### Robust Error Handling

```python
from bluesky_util import BlueSkyFollowers

def safe_get_followers(username, limit=100):
    """Safely get followers with comprehensive error handling"""
    bf = BlueSkyFollowers()
    
    try:
        # Validate username format first
        if '.' not in username:
            return {
                'success': False,
                'error': 'Username must include domain (e.g., user.bsky.social)'
            }
        
        # Get followers data
        data = bf.get_followers_data(username, limit=limit)
        
        if data['success']:
            print(f"✓ Successfully retrieved {len(data['followers'])} followers")
            return data
        else:
            print(f"✗ API Error: {data['error']}")
            return data
            
    except ValueError as e:
        # Username validation error
        error_msg = f"Username validation error: {e}"
        print(f"✗ {error_msg}")
        return {'success': False, 'error': error_msg}
        
    except Exception as e:
        # Unexpected error
        error_msg = f"Unexpected error: {e}"
        print(f"✗ {error_msg}")
        return {'success': False, 'error': error_msg}

# Example usage with error handling
result = safe_get_followers('jack.bsky.social', limit=50)
if result['success']:
    followers = result['followers']
    # Process followers...
```

### Batch Processing with Error Handling

```python
from bluesky_util import BlueSkyFollowers
import time

def batch_process_users(usernames, limit=50, delay=1):
    """Process multiple users with error handling and rate limiting"""
    bf = BlueSkyFollowers()
    results = {}
    
    for i, username in enumerate(usernames, 1):
        print(f"Processing {i}/{len(usernames)}: @{username}")
        
        try:
            data = bf.get_followers_data(username, limit=limit)
            
            if data['success']:
                results[username] = {
                    'status': 'success',
                    'follower_count': len(data['followers']),
                    'target_info': data['target_user']
                }
                print(f"  ✓ {len(data['followers'])} followers retrieved")
            else:
                results[username] = {
                    'status': 'api_error',
                    'error': data['error']
                }
                print(f"  ✗ API Error: {data['error']}")
                
        except Exception as e:
            results[username] = {
                'status': 'exception',
                'error': str(e)
            }
            print(f"  ✗ Exception: {e}")
        
        # Rate limiting
        if i < len(usernames):  # Don't sleep after the last user
            time.sleep(delay)
    
    return results

# Example usage
usernames = [
    'jack.bsky.social',
    'invalid-user',  # This will cause an error
    'pfrazee.com'
]

results = batch_process_users(usernames, limit=25, delay=2)

# Summary
successful = sum(1 for r in results.values() if r['status'] == 'success')
print(f"\nBatch complete: {successful}/{len(usernames)} successful")
```

## Integration Examples

### Django Integration

```python
# models.py
from django.db import models
from bluesky_util import BlueSkyFollowers
import json

class BlueSkyUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    display_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    follower_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    def update_from_bluesky(self):
        """Update user data from BlueSky API"""
        bf = BlueSkyFollowers()
        profile = bf.get_user_profile(self.username)
        
        if profile:
            self.display_name = profile.display_name or ''
            self.description = profile.description or ''
            self.follower_count = getattr(profile, 'followers_count', 0)
            self.following_count = getattr(profile, 'follows_count', 0)
            self.save()
            return True
        return False

class FollowerSnapshot(models.Model):
    user = models.ForeignKey(BlueSkyUser, on_delete=models.CASCADE)
    snapshot_date = models.DateTimeField(auto_now_add=True)
    follower_data = models.JSONField()
    total_followers = models.IntegerField()
    
    @classmethod
    def create_snapshot(cls, username, limit=100):
        """Create a follower snapshot"""
        bf = BlueSkyFollowers()
        data = bf.get_followers_data(username, limit=limit)
        
        if data['success']:
            user, created = BlueSkyUser.objects.get_or_create(
                username=username,
                defaults={
                    'display_name': data['target_user']['display_name'],
                    'description': data['target_user']['description'],
                    'follower_count': data['target_user']['follower_count'],
                    'following_count': data['target_user']['following_count']
                }
            )
            
            snapshot = cls.objects.create(
                user=user,
                follower_data=data['followers'],
                total_followers=len(data['followers'])
            )
            
            return snapshot
        return None
```

### Flask Web App

```python
# app.py
from flask import Flask, render_template, request, jsonify
from bluesky_util import BlueSkyFollowers

app = Flask(__name__)
bf = BlueSkyFollowers()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/followers/<username>')
def get_followers_api(username):
    limit = request.args.get('limit', 50, type=int)
    
    try:
        data = bf.get_followers_data(username, limit=limit)
        return jsonify(data)
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/user/<username>')
def user_page(username):
    limit = request.args.get('limit', 50, type=int)
    data = bf.get_followers_data(username, limit=limit)
    
    if data['success']:
        return render_template('user.html', data=data)
    else:
        return render_template('error.html', error=data['error'])

if __name__ == '__main__':
    app.run(debug=True)
```

## Advanced Usage

### Custom Data Processing Pipeline

```python
from bluesky_util import BlueSkyFollowers
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

class BlueSkyAnalyzer:
    def __init__(self):
        self.bf = BlueSkyFollowers()
    
    def get_follower_dataframe(self, username, limit=500):
        """Get followers as a pandas DataFrame"""
        data = self.bf.get_followers_data(username, limit=limit)
        
        if not data['success']:
            raise ValueError(f"Failed to get data: {data['error']}")
        
        # Convert to DataFrame
        df = pd.DataFrame(data['followers'])
        
        # Add additional columns
        df['joined_date_parsed'] = pd.to_datetime(df['joined_date_raw'])
        df['description_length'] = df['description'].str.len().fillna(0)
        df['has_display_name'] = df['display_name'].notna() & (df['display_name'] != '')
        
        return df, data['target_user']
    
    def analyze_follower_patterns(self, username, limit=500):
        """Comprehensive follower analysis"""
        df, target = self.get_follower_dataframe(username, limit)
        
        analysis = {
            'target_user': target,
            'total_analyzed': len(df),
            'join_date_stats': {
                'earliest': df['joined_date_parsed'].min(),
                'latest': df['joined_date_parsed'].max(),
                'median': df['joined_date_parsed'].median()
            },
            'profile_completeness': {
                'with_display_name': df['has_display_name'].sum(),
                'with_description': (df['description_length'] > 0).sum(),
                'avg_description_length': df['description_length'].mean()
            },
            'monthly_growth': df.groupby(df['joined_date_parsed'].dt.to_period('M')).size().to_dict()
        }
        
        return analysis, df
    
    def plot_growth_chart(self, username, limit=500, save_path=None):
        """Create a growth visualization"""
        analysis, df = self.analyze_follower_patterns(username, limit)
        
        # Prepare monthly data
        monthly_data = df.groupby(df['joined_date_parsed'].dt.to_period('M')).size()
        monthly_data.index = monthly_data.index.to_timestamp()
        
        # Create plot
        plt.figure(figsize=(12, 6))
        plt.plot(monthly_data.index, monthly_data.values, marker='o')
        plt.title(f'Monthly Follower Growth - @{username}')
        plt.xlabel('Month')
        plt.ylabel('New Followers')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        else:
            plt.show()

# Example usage
analyzer = BlueSkyAnalyzer()

# Get detailed analysis
analysis, df = analyzer.analyze_follower_patterns('jack.bsky.social', limit=200)

print(f"Analysis for @{analysis['target_user']['handle']}")
print(f"Total followers analyzed: {analysis['total_analyzed']}")
print(f"Followers with display names: {analysis['profile_completeness']['with_display_name']}")
print(f"Average description length: {analysis['profile_completeness']['avg_description_length']:.1f} chars")

# Create growth chart
analyzer.plot_growth_chart('jack.bsky.social', limit=200, save_path='growth_chart.png')
```

### Monitoring and Alerting

```python
from bluesky_util import BlueSkyFollowers
import time
import json
from datetime import datetime

class FollowerMonitor:
    def __init__(self, config_file='monitor_config.json'):
        self.bf = BlueSkyFollowers()
        self.config = self.load_config(config_file)
        self.history = {}
    
    def load_config(self, config_file):
        """Load monitoring configuration"""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                'users_to_monitor': [],
                'check_interval': 3600,  # 1 hour
                'alert_threshold': 10    # Alert if +/- 10 followers
            }
    
    def check_user(self, username):
        """Check a single user for changes"""
        try:
            profile = self.bf.get_user_profile(username)
            
            if not profile:
                return {'error': 'User not found'}
            
            current_count = getattr(profile, 'followers_count', 0)
            timestamp = datetime.now().isoformat()
            
            result = {
                'username': username,
                'timestamp': timestamp,
                'follower_count': current_count,
                'display_name': profile.display_name or '',
                'change': 0
            }
            
            # Check for changes
            if username in self.history:
                last_count = self.history[username]['follower_count']
                result['change'] = current_count - last_count
            
            # Update history
            self.history[username] = result
            
            return result
            
        except Exception as e:
            return {'error': str(e)}
    
    def monitor_all(self):
        """Monitor all configured users"""
        results = []
        
        for username in self.config['users_to_monitor']:
            print(f"Checking @{username}...")
            result = self.check_user(username)
            results.append(result)
            
            # Check for significant changes
            if 'change' in result and abs(result['change']) >= self.config['alert_threshold']:
                self.send_alert(result)
            
            time.sleep(1)  # Rate limiting
        
        return results
    
    def send_alert(self, result):
        """Send alert for significant changes"""
        change = result['change']
        username = result['username']
        count = result['follower_count']
        
        if change > 0:
            message = f"🔥 @{username} gained {change} followers (now {count})"
        else:
            message = f"📉 @{username} lost {abs(change)} followers (now {count})"
        
        print(f"ALERT: {message}")
        # Here you could integrate with Slack, Discord, email, etc.
    
    def run_continuous(self):
        """Run continuous monitoring"""
        print(f"Starting follower monitor for {len(self.config['users_to_monitor'])} users")
        print(f"Check interval: {self.config['check_interval']} seconds")
        
        while True:
            try:
                results = self.monitor_all()
                
                # Log results
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"[{timestamp}] Monitoring cycle complete")
                
                time.sleep(self.config['check_interval'])
                
            except KeyboardInterrupt:
                print("\nMonitoring stopped by user")
                break
            except Exception as e:
                print(f"Error in monitoring cycle: {e}")
                time.sleep(60)  # Wait a minute before retrying

# Example usage
monitor = FollowerMonitor()

# Add users to monitor
monitor.config['users_to_monitor'] = [
    'jack.bsky.social',
    'pfrazee.com',
    'jay.bsky.social'
]

# Run a single check
results = monitor.monitor_all()
for result in results:
    if 'error' not in result:
        print(f"@{result['username']}: {result['follower_count']} followers ({result['change']:+d})")
```

These examples demonstrate the versatility and power of the BlueSky Followers Utility v2.0.0. The library architecture makes it easy to integrate into larger applications and build sophisticated analysis tools.
