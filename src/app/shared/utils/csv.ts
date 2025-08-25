import { Task } from '../models/task.model';

const header =
  'id,title,description,dueDate,priority,status,createdAt,updatedAt';

export function stringifyCSV(tasks: Task[]): string {
  const escape = (val: string) =>
    `"${String(val ?? '').replace(/"/g, '""')}"`;

  const lines = tasks.map(t => [
    t.id, t.title, t.description, t.dueDate, t.priority, t.status, t.createdAt, t.updatedAt
  ].map(escape).join(','));

  return [header, ...lines].join('\n');
}

export function parseCSV(csv: string): Task[] {
  if (!csv || !csv.trim()) return [];
  const lines = csv.split(/\r?\n/).filter(l => l.trim().length > 0);
  const [hdr, ...rows] = lines;
  if (!hdr.toLowerCase().startsWith('id,')) return []; // guard against wrong file

  const parseLine = (line: string): string[] => {
    const out: string[] = [];
    let cur = '', inQuote = false;
    for (let i = 0; i < line.length; i++) {
      const ch = line[i];
      if (inQuote) {
        if (ch === '"' && line[i + 1] === '"') { cur += '"'; i++; }
        else if (ch === '"') inQuote = false;
        else cur += ch;
      } else {
        if (ch === '"') inQuote = true;
        else if (ch === ',') { out.push(cur); cur = ''; }
        else cur += ch;
      }
    }
    out.push(cur);
    return out;
  };

  return rows.map(row => {
    const [id, title, description, dueDate, priority, status, createdAt, updatedAt] = parseLine(row);
    return { id, title, description, dueDate, priority: priority as any, status: status as any, createdAt, updatedAt };
  });
}
