import { useCallback, useEffect, useState } from "react";

export const useModal = () => {
  const [modalOpen, setModalOpen] = useState(false);

  const open = useCallback(() => {
    setModalOpen(true);
  }, []);

  const close = useCallback(() => {
    setModalOpen(false);
  }, []);

  useEffect(() => {
    if (typeof document !== "undefined") {
      document.body.style.overflow = modalOpen ? "hidden" : "";
    }
  }, [modalOpen]);

  useEffect(() => {
    if (typeof window !== "undefined") {
      const handleCloseModal = (event: KeyboardEvent) => {
        if (event.key === "Escape") {
          close();
        }
      };
      window.addEventListener("keyup", handleCloseModal);
      return () => window.removeEventListener("keyup", handleCloseModal);
    }
  }, [close]);

  return {
    toggle: () => (modalOpen ? close() : open()),
    isOpen: modalOpen,
  };
};
