import { useStartups } from "@/hooks/useStartups";
import { useEffect } from "react";
import { toast } from "sonner";
import { StartupCard } from "../components/composed_ui/StartupCard";

export function Startups() {
  const { data, isLoading, isError, error } = useStartups();

  useEffect(() => {
    if (isError) {
      toast.error(error?.response?.data?.detail || "Щось пішло не так, спробуйте ще раз");
    }
  }, [isError, error]);

  if (isLoading) return <div>Loading...</div>;

  if (isError || !data) return <div>Error loading startups.</div>;
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-8">
      {data.map((startup) => (
        <StartupCard key={startup.id} startup={startup} />
      ))}
    </div>
  );
}
