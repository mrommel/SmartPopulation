"""

def simulation_to_database(sim: Simulation):
	database = get_db()

	# polices
	for key, policy in sim.policies.items():
		database.execute(
			'UPDATE policies SET is_active = ?, slider_value = ?, value = ? WHERE key = ?',
			(policy.is_active, policy.slider_value, policy.value, key)
		)
		database.commit()
		
		policy_row = database.execute(
			'SELECT p.id FROM policies AS p WHERE key = ?',
			(key,)
		).fetchone()
		if policy_row is None:
			raise Exception(f'cant find policy "{key}" in db')
		
		policy_id = policy_row[0]
		
		database.execute(
			'DELETE FROM policy_histories WHERE policy_id = ?',
			(policy_id,)
		)
		database.commit()
		
		for policy_history_value in policy.history:
			database.execute(
				'INSERT INTO policy_histories (policy_id, value) VALUES (?, ?)',
				(policy_id, policy_history_value)
			)
			database.commit()
		
	# groups
	for key, group in sim.groups.items():
		
		group_row = database.execute(
			'SELECT g.id FROM groups AS g WHERE g.key = ?', (key,)
		).fetchone()
		if group_row is None:
			raise Exception(f'cant find group "{key}" in db')
		
		group_id = group_row[0]
		
		database.execute(
			'DELETE FROM group_histories WHERE group_id = ?', (group_id,)
		)
		database.commit()
		
		for index in range(0, len(group.mood.history)):
			group_mood_history_value = group.mood.history[index]
			group_freq_history_value = group.mood.history[index]
			database.execute(
				'INSERT INTO group_histories (group_id, mood_value, freq_value) VALUES (?, ?, ?)',
				(group_id, group_mood_history_value, group_freq_history_value)
			)
			database.commit()
"""
